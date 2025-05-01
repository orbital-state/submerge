from .base import BaseDivProp

class TestsProp(BaseDivProp):
    """
    Tests property class.

    This class is used to represent tests-related properties.
    """
    def __init__(self, name: str):
        assert name == 'tests',  f"Invalid name: {name}. Expected 'tests'"
        super().__init__('tests')