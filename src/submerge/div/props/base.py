import os


class BaseDivProp:
    """
    Base class for all properties.
    """

    def __init__(self, name: str):
        self.name = name
        self.payload = None

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name})"
    
    def load(self, node_path: str):
        """
        Load the property payload from a given node path.
        
        This is a universal data loading method from any container.
        It can load from YAML, JSON, DIV, or any other format.
        Or even a folder if `index.<format>` files is present.
        The method can be overridden in subclasses to provide specific loading logic.
        """
        # Check if the node path exists and is a directory
        if not os.path.isdir(node_path):
            raise FileNotFoundError(f"Node path does not exist or is not a directory: {node_path}")
        