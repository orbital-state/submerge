from .base import BaseDivProp

class HistoryProp(BaseDivProp):
    """
    History property class.

    This class is used to represent history-related properties.
    """
    def __init__(self, name: str):
        assert name == 'history', f"Invalid name: {name}. Expected 'history'."
        super().__init__('history')