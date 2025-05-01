from .base import BaseDivProp

class ContractsProp(BaseDivProp):
    """
    Contracts property class.

    This class is used to represent contracts-related properties.
    """
    def __init__(self, name: str):
        assert name == 'contracts', f"Invalid name: {name}. Expected 'contracts'."
        super().__init__('contracts')