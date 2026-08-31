import asyncio
from typing import Dict, Any

from backend.verification.evaluator import OutputValidator
from backend.services.knowledge_graph import KnowledgeGraphIngestor
from backend.services.vector_cache import VectorCache
from backend.services.memory import MemoryEcosystem
from backend.routing.dynamic_router import DynamicRouter 

class SelfLearningEngine:
    def __init__(self):
        self.router = DynamicRouter()
        self.validator = OutputValidator()
        self.kg = KnowledgeGraphIngestor()
        self.cache = VectorCache()
        self.memory = MemoryEcosystem()

    async def execute_cycle(self, task: Dict[str, Any]) -> Dict[str, Any]:
        agent = self.router.route_task(task.get("prompt", ""), task.get("category", "reasoning"))
        
        # Safely extract the model to prevent KeyError
        model_name = agent.get("model", "default_model") if isinstance(agent, dict) else "default_model"
        output = f"Execution result for model ({model_name})"
        
        audit_result = await self.validator.verify_output(task, output)

        if not audit_result.get("passed", True):
            refinement = {"corrected_output": "Optimal execution refinement."}
            student_output = output
            feedback = audit_result.get("feedback", "")
            
            # Store failed pattern for synthesis using a safe .get() for the ID
            await self.memory.cache_working_state(task.get("id", "task_fallback"), student_output)
            return refinement

        self.kg.add_node(task.get("id", "task_0"), audit_result)
        return {"status": "completed", "output": output, "audit": audit_result}

    async def run_continuous_loop(self):
        """Automated background training loop for agent alignment."""
        while True:
            unresolved_tasks = await self.memory.get_unprocessed_logs()
            
            if not unresolved_tasks:
                task = {"id": "task_1", "prompt": "Continuous learning sample", "category": "reasoning"}
                await self.execute_cycle(task)
            else:
                for task in unresolved_tasks:
                    await self.execute_cycle(task)
                    
            await asyncio.sleep(5)  # Cycle delay
