from typing import Dict, Any

class DynamicRouter:
    def __init__(self):
        self.providers = {"code": "DeepSeek", "math": "GPT-4o", "reasoning": "Claude-3.5"}

    def route_task(self, prompt: str, category: str) -> Dict[str, str]:
        selected_model = self.providers.get(category, "GPT-4o")
        return {"model": selected_model, "status": "routed", "prompt": prompt}
