from .base import BaseDivProp

class ResponseProp(BaseDivProp):
    """
    Response property class.

    This class is used to represent response-related properties.
    """
    def __init__(self, name: str):
        assert name == 'response',  f"Invalid name: {name}. Expected 'response'"
        super().__init__('response')