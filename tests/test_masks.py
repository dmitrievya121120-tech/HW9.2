import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def valid_accounts():
    """Пример корректных номеров счетов для тестов."""
    return [
        73654108430135874305,
        123456789012,
    ]


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (7000792289606361, "7000 79** **** 6361"),
        (1234567812345678, "1234 56** **** 5678"),
    ],
)
def test_get_mask_card_number_valid_param(card_number, expected) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "card_number",
    [
        123456789012345,
        12345678901234567,
    ],
)
def test_get_mask_card_number_invalid_param(card_number) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize(
    "account, expected",
    [
        (73654108430135874305, "**4305"),
        (123456789012, "**9012"),
    ],
)
def test_get_mask_account_valid_param(account, expected) -> None:
    assert get_mask_account(account) == expected


def test_get_mask_account_invalid() -> None:
    """Тест маскировки номера счета с некорректными данными."""
    with pytest.raises(ValueError):
        get_mask_account(123)


def test_mask_functions_type_annotations(valid_accounts) -> None:
    """Проверка, что функции возвращают строки (используем фикстуру)."""
    result_card = get_mask_card_number(7000792289606361)
    result_account_1 = get_mask_account(valid_accounts[0])
    result_account_2 = get_mask_account(valid_accounts[1])

    assert isinstance(result_card, str)
    assert isinstance(result_account_1, str)
    assert isinstance(result_account_2, str)
