from .base import BaseDivProp

class PromptsProp(BaseDivProp):
    """
    Prompts property class.

    This class is used to represent prompts-related properties.
    """
    def __init__(self, name: str):
        assert name == 'prompts', f"Invalid name: {name}. Expected 'prompts'."
        super().__init__('prompts')