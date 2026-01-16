from collections.abc import Generator
from typing import Any, Dict, Iterable


def filter_by_currency(
    transactions: Iterable[Dict[str, Any]],
    currency: str,
) -> Generator[Dict[str, Any], None, None]:
    """
    Генератор, который возвращает только операции с указанной валютой.

    Ожидается структура:
    {
        "operationAmount": {
            "amount": "100.00",
            "currency": {"name": "USD", "code": "USD"},
        },
        ...
    }
    """
    for tx in transactions:
        code = (
            tx.get("operationAmount", {})
            .get("currency", {})
            .get("code")
        )
        if code == currency:
            yield tx


def transaction_descriptions(
    transactions: Iterable[Dict[str, Any]],
) -> Generator[str, None, None]:
    """
    Генератор, который последовательно отдаёт описания операций по ключу 'description'.
    """
    for tx in transactions:
        description = tx.get("description")
        if description is not None:
            yield description


def card_number_generator(
    start: int,
    count: int,
) -> Generator[str, None, None]:
    """
    Генерирует 'count' номеров карт, начиная с 'start',
    в формате 'XXXX XXXX XXXX XXXX'.
    """
    current = start
    for _ in range(count):
        num_str = f"{current:016d}"
        formatted = " ".join(
            [num_str[i : i + 4] for i in range(0, 16, 4)]
        )
        yield formatted
        current += 1
