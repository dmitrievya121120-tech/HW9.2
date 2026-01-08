import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_valid() -> None:
    """Тест маскировки номера карты с корректными данными."""
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"
    assert get_mask_card_number(1234567812345678) == "1234 56** **** 5678"


def test_get_mask_card_number_invalid() -> None:
    """Тест маскировки номера карты с некорректными данными."""
    with pytest.raises(ValueError):
        get_mask_card_number(123456789012345)

    with pytest.raises(ValueError):
        get_mask_card_number(12345678901234567)


def test_get_mask_account_valid() -> None:
    """Тест маскировки номера счета с корректными данными."""
    assert get_mask_account(73654108430135874305) == "**4305"
    assert get_mask_account(123456789012) == "**9012"


def test_get_mask_account_invalid() -> None:
    """Тест маскировки номера счета с некорректными данными."""
    with pytest.raises(ValueError):
        get_mask_account(123)


def test_mask_functions_type_annotations() -> None:
    """Проверка, что функции возвращают строки."""
    result_card = get_mask_card_number(7000792289606361)
    result_account = get_mask_account(73654108430135874305)

    assert isinstance(result_card, str)
    assert isinstance(result_account, str)
