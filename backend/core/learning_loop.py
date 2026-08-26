import asyncio
from typing import Dict, Any, List
from backend.managers.routing import GlobalMultiplexer
from backend.verification.evaluator import OutputValidator
from backend.services.memory import MemoryEcosystem

class SelfLearningEngine:
    def __init__(self):
        self.router = GlobalMultiplexer()
        self.validator = OutputValidator()
        self.memory = MemoryEcosystem()

    async def execution_cycle(self, task: Dict[str, Any]) -> Dict[str, Any]:
        # 1. Routing task to specialized agent
        agent = self.router.select_agent(task)
        initial_output = await agent.execute(task)

        # 2. Peer Verification / Cross-Evaluation
        audit_result = await self.validator.verify_output(
            task=task, output=initial_output
        )

        # 3. Recursive Learning Loop
        if not audit_result["passed"]:
            # Corrective teaching interaction
            refinement = await self.router.get_teacher_agent().teach(
                student_output=initial_output, 
                feedback=audit_result["feedback"]
            )
            
            # Store teaching pattern to long-term memory graph
            await self.memory.store_embedding(
                key=task["task_id"],
                vector=refinement["learning_vector"]
            )
            
            return refinement["corrected_output"]

        # Store successful pattern for synthesis
        await self.memory.cache_working_state(task["task_id"], initial_output)
        return initial_output

    async def run_continuous_loop(self):
        """Automated background training loop for agent alignment."""
        while True:
            unresolved_tasks = await self.memory.get_unprocessed_logs()
            for task in unresolved_tasks:
                await self.execution_cycle(task)
            await asyncio.sleep(5)  # Cycle delay
