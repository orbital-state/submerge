from .base import BaseDivProp

class ImplsProp(BaseDivProp):
    """
    Implementations property class.

    This class is used to represent implementation-related properties.
    """
    def __init__(self, name: str):
        assert name == 'impls',  f"Invalid name: {name}. Expected 'impls'"
        super().__init__('impls')