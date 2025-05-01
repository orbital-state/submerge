import os
from .base import BaseDivProp
from ...utils.div_asserts import is_div_node
from logging import getLogger
logger = getLogger(__name__)


class ThreadsProp(BaseDivProp):
    """
    Threads property class.

    This class is used to represent threads-related properties.
    """
    def __init__(self, name: str):
        assert name == 'threads', f"Invalid name: {name}. Expected 'threads'."
        self.name = 'threads'
        self._children = []
    
    def load(self, node_path: str):
        """
        Load the threads property as a list of child subfolders other than '.div'.

        Children must be valid DIV nodes themselves (i.e. contain a `.div` subfolder).
        """
        # Check if the node path exists and is a directory
        if not os.path.isdir(node_path):
            raise FileNotFoundError(f"Node path does not exist or is not a directory: {node_path}")
        
        # Iterate over the contents of the node path
        for item in os.listdir(node_path):
            item_path = os.path.join(node_path, item)
            # Check if the item is a directory and not the .div folder
            if os.path.isdir(item_path) and item != ".div":
                # check if the item is a valid DIV node
                if is_div_node(item_path):
                    # Append the item to the children list
                    self._children.append(item)
                else:
                    logger.debug(f"Item is not a valid DIV node: {item_path}")

    @property
    def payload(self):
        """
        Return the payload of the threads property.
        
        The payload is a list of child subfolders other than '.div'.
        """
        return self._children