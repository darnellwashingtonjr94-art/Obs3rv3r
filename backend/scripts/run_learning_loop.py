import asyncio
from backend.core.learning_loop import SelfLearningEngine

async def main():
    engine = SelfLearningEngine()
    print("Starting automated self-learning execution cycle...")
    await engine.run_continuous_loop()

if __name__ == "__main__":
    asyncio.run(main())
