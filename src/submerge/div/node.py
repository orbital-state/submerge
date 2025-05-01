import os
import logging
from ..utils.div_asserts import is_div_node
from .props.undefined import UndefinedProp
from .props.factory import PropFactory

logger = logging.getLogger(__name__)


class DivNode:

    def __init__(self, node_path):
        if not os.path.exists(node_path):
            raise FileNotFoundError(f"Node path does not exist: {node_path}")
        if not os.path.isdir(node_path):
            raise NotADirectoryError(f"Node path is not a directory: {node_path}")
        if not is_div_node(node_path):
            raise ValueError(f"Node path is not a valid DIV node: {node_path}")
        self.node_path = node_path
        self.name = os.path.basename(node_path)
        # Data model is a dynamic list of property names
        self.properties: dict = {
            'threads': UndefinedProp('undefined'),
            'metadata': UndefinedProp('undefined'),
            'contracts': UndefinedProp('undefined'),
            'prompts': UndefinedProp('undefined'),
            'history': UndefinedProp('undefined'),
            'impls': UndefinedProp('undefined'),
            'tests': UndefinedProp('undefined'),
            'reasoning': UndefinedProp('undefined'),
            'response': UndefinedProp('undefined'),
        }
    

    def load(self):
        """
        Load and populate the properties of the DivNode from the node folder path.
        """
        # Iterate over the properties and load them from the node path
        for prop_name in self.properties:
            prop = PropFactory.create_prop(prop_name)
            if prop:
                prop.load(self.node_path)
                self.properties[prop_name] = prop
            else:
                raise ValueError(f"Unknown property name: {prop_name}")
        