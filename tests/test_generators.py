import pytest

from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "description": "Перевод организации",
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "RUB", "code": "RUB"},
            },
        },
        {
            "id": 2,
            "description": "Покупка",
            "operationAmount": {
                "amount": "10.00",
                "currency": {"name": "USD", "code": "USD"},
            },
        },
        {
            "id": 3,
            "description": "Перевод со счета на счет",
            "operationAmount": {
                "amount": "5.00",
                "currency": {"name": "USD", "code": "USD"},
            },
        },
    ]


def test_filter_by_currency_usd(sample_transactions):
    usd_txs = list(filter_by_currency(sample_transactions, "USD"))

    assert [tx["id"] for tx in usd_txs] == [2, 3]


def test_filter_by_currency_empty(sample_transactions):
    eur_txs = list(filter_by_currency(sample_transactions, "EUR"))

    assert eur_txs == []


def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))

    assert descriptions == [
        "Перевод организации",
        "Покупка",
        "Перевод со счета на счет",
    ]


def test_card_number_generator_sequence():
    gen = card_number_generator(1, 3)
    numbers = list(gen)

    assert numbers == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]
