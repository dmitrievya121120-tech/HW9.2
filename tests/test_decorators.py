import logging
from pathlib import Path

import pytest

from src.decorators import log


def test_log_console_logs_start_and_finish(caplog: pytest.LogCaptureFixture) -> None:
    @log()
    def add(a: int, b: int) -> int:
        return a + b

    with caplog.at_level(logging.INFO):
        result = add(2, 3)

    assert result == 5
    text = caplog.text
    assert "Start function add" in text
    assert "Function add finished, returned 5" in text


def test_log_logs_exception(caplog: pytest.LogCaptureFixture) -> None:
    @log()
    def div(a: int, b: int) -> float:
        return a / b

    with caplog.at_level(logging.ERROR), pytest.raises(ZeroDivisionError):
        div(1, 0)

    assert "Function div raised" in caplog.text


def test_log_to_file(tmp_path: Path) -> None:
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def mul(a: int, b: int) -> int:
        return a * b

    result = mul(2, 4)
    assert result == 8

    content = log_file.read_text(encoding="utf-8")
    assert "Start function mul" in content
    assert "Function mul finished, returned 8" in content
