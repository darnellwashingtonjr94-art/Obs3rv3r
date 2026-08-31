import os
import json
from typing import Dict, Any

class KnowledgeGraphIngestor:
    def __init__(self, storage_path: str = "data/knowledge_graphs/nodes.json"):
        self.storage_path = storage_path
        self._ensure_dir()

    def _ensure_dir(self):
        """Creates parent directory tree if it does not exist."""
        directory = os.path.dirname(self.storage_path)
        if directory:
            os.makedirs(directory, exist_ok=True)

    def add_node(self, node_id: str, data: Dict[str, Any]):
        self._ensure_dir()
        with open(self.storage_path, "a") as f:
            f.write(json.dumps({"id": node_id, "data": data}) + "\n")
