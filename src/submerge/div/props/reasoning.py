from .base import BaseDivProp

class ReasoningProp(BaseDivProp):
    """
    Reasoning property class.

    This class is used to represent reasoning-related properties.
    """
    def __init__(self, name: str):
        assert name == 'reasoning', f"Invalid name: {name}. Expected 'reasoning'."
        super().__init__('reasoning')