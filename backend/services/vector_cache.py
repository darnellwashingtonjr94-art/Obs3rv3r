class VectorCache:
    def __init__(self):
        self.cache = {}

    def set_embedding(self, task_hash: str, vector: list):
        self.cache[task_hash] = vector

    def get_embedding(self, task_hash: str) -> list:
        return self.cache.get(task_hash, [])
