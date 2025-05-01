from .base import BaseDivProp

class MetadataProp(BaseDivProp):
    """
    Metadata property class.

    This class is used to represent metadata-related properties.
    """
    def __init__(self, name: str):
        assert name == 'metadata', f"Invalid name: {name}. Expected 'metadata'."
        super().__init__('metadata')