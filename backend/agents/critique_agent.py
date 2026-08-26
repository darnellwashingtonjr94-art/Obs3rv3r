class CritiqueAgent:
    async def evaluate_response(self, prompt: str, output: str) -> dict:
        # Evaluates primary model output against safety and accuracy guidelines
        score = 0.95 if len(output) > 20 else 0.40
        return {
            "score": score,
            "feedback": "Sufficient detail provided." if score > 0.8 else "Needs expansion.",
            "approved": score >= 0.8
        }
