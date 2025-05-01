class DivError(Exception):
    def __init__(self, message="An error occurred in the Div project."):
        super().__init__(message)
