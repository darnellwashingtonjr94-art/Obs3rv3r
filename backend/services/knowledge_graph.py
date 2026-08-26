import json

class KnowledgeGraphIngestor:
    def __init__(self, storage_path: str = "data/knowledge_graphs/nodes.json"):
        self.storage_path = storage_path

    def add_node(self, node_id: str, attributes: dict):
        # Appends extracted agent learnings to local graph schema
        data = {node_id: attributes}
        with open(self.storage_path, "a") as f:
            f.write(json.dumps(data) + "\n")
