import logging

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

def set_logging_level(logger: logging.Logger, verbosity: int):
    if verbosity >= 3:
        logger.setLevel(logging.DEBUG)
    elif verbosity == 2:
        logger.setLevel(logging.INFO)
    elif verbosity == 1:
        logger.setLevel(logging.WARNING)
    else:
        logger.setLevel(logging.ERROR)

def is_debug_mode(logger: logging.Logger) -> bool:
    """
    Check if the logger is in DEBUG mode.
    """
    return logger.getEffectiveLevel() == logging.DEBUG
