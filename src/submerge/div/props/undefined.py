from .base import BaseDivProp

class UndefinedProp(BaseDivProp):
    """
    Undefined property class.
    
    This class is used to represent properties that are not defined or have no specific implementation.
    It serves as a placeholder and does not perform any operations.
    """
    def __init__(self, name: str):
        assert name == 'undefined', f"Invalid name: {name}. Expected 'undefined'."
        super().__init__('undefined')