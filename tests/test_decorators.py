import logging

import pytest

from src.decorators import log


def test_log_returns_result(caplog: pytest.LogCaptureFixture) -> None:
    @log
    def add(a: int, b: int) -> int:
        return a + b

    with caplog.at_level(logging.INFO):
        result = add(2, 3)

    assert result == 5
    assert "Function add returned 5" in caplog.text


def test_log_logs_exception(caplog: pytest.LogCaptureFixture) -> None:
    @log
    def div(a: int, b: int) -> float:
        return a / b

    with caplog.at_level(logging.ERROR), pytest.raises(ZeroDivisionError):
        div(1, 0)

    assert "Function div raised" in caplog.text
