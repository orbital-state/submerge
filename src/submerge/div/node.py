import json
import os

class DivNode:
    def __init__(self, node_path):
        self.name = None
        self.type = None
        self.metadata = {}
        self.content = None

    def load(self, file_path):
        """
        Load and populate the properties of the DivNode from current branch folder.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, 'r') as file:
            data = json.load(file)

        self.name = data.get("name")
        self.type = data.get("type")
        self.metadata = data.get("metadata", {})
        self.content = data.get("content")
