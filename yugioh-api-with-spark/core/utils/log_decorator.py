from functools import wraps

from loguru import logger


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(
            f"Calling function '{func.__name__}' with args {args} and kwargs {kwargs}"
        )
        try:
            result = func(*args, **kwargs)
            logger.info(f"'{func.__name__}' function returned {result}")
            return result
        except Exception as e:
            logger.exception(f"Exception caught in '{func.__name__}': {e}")
            raise

    return wrapper
