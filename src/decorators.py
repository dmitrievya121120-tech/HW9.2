import functools
import logging
from typing import Any, Callable


logger = logging.getLogger(__name__)


def log(func: Callable) -> Callable:
    """
    Декоратор логирует успешный результат выполнения функции
    и информацию об исключении, если оно произошло.
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            result = func(*args, **kwargs)
            logger.info("Function %s returned %r", func.__name__, result)
            return result
        except Exception as exc:
            logger.error("Function %s raised %r", func.__name__, exc)
            raise

    return wrapper
