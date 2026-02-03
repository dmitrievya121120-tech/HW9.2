import functools
import logging
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Логирует начало и конец выполнения функции, а также исключения.

    :param filename: путь к файлу для логов; если None — логируем в консоль.
    """

    def decorator(func: Callable) -> Callable:
        logger = logging.getLogger(f"{__name__}.{func.__name__}")
        logger.setLevel(logging.INFO)

        if filename:
            handler: logging.Handler = logging.FileHandler(filename, encoding="utf-8")
        else:
            handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)

        if not logger.handlers:
            logger.addHandler(handler)

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger.info("Start function %s", func.__name__)
            try:
                result = func(*args, **kwargs)
                logger.info("Function %s finished, returned %r", func.__name__, result)
                return result
            except Exception as exc:
                logger.error("Function %s raised %r", func.__name__, exc)
                raise

        return wrapper

    return decorator
