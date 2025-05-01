from .base import BaseDivProp
from .undefined import UndefinedProp
from .metadata import MetadataProp
from .threads import ThreadsProp
from .contracts import ContractsProp
from .prompts import PromptsProp
from .history import HistoryProp
from .impls import ImplsProp
from .tests import TestsProp
from .reasoning import ReasoningProp
from .response import ResponseProp


mapping = {
    'undefined': UndefinedProp,
    'metadata': MetadataProp,
    'threads': ThreadsProp,
    'contracts': ContractsProp,
    'prompts': PromptsProp,
    'history': HistoryProp,
    'impls': ImplsProp,
    'tests': TestsProp,
    'reasoning': ReasoningProp,
    'response': ResponseProp,
}

class PropFactory:
    """
    Factory class for creating property instances.
    """
    @staticmethod
    def create_prop(name: str) -> 'BaseDivProp':
        """
        Factory method to create a Prop instance for a given node path.
        """
        if name not in mapping:
            raise ValueError(f"Invalid property name: {name}")

        # Dynamically import the class based on the mapping
        module_name = f".props.{name}"
        # class_name = mapping[name]
        prop_class = mapping[name]

        try:
            # module = __import__(module_name, fromlist=[class_name])
            # prop_class = getattr(module, class_name)
            return prop_class(name)
        except (ImportError, AttributeError) as e:
            raise ImportError(f"Failed to import or initialize property class '{class_name}' from module '{module_name}': {e}")
