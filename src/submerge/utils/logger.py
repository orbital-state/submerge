import logging

def get_logger(name: str) -> logging.Logger:
    """
    Set up and return a logger with the specified name.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:  # Avoid adding multiple handlers
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

def set_logging_level(logger: logging.Logger, verbosity: int):
    """
    Set the logging level based on verbosity.
    """
    if verbosity == 0:
        logger.setLevel(logging.WARNING)
    elif verbosity == 1:
        logger.setLevel(logging.INFO)
    elif verbosity == 2:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.NOTSET)
    logger.info(f"Logging level set to {logging.getLevelName(logger.level)}")