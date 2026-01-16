import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "raw, expected",
    [
        (
            "Visa Platinum 7000792289606361",
            "Visa Platinum 7000 79** **** 6361",
        ),
        (
            "Maestro 7000792289606361",
            "Maestro 7000 79** **** 6361",
        ),
    ],
)
def test_mask_account_card_for_cards(raw, expected):
    assert mask_account_card(raw) == expected


def test_mask_account_card_for_account():
    raw = "Счет 73654108430135874305"
    expected = "Счет **4305"  # ожидаемый формат из masks.get_mask_account

    assert mask_account_card(raw) == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2020-01-01T00:00:00", "01.01.2020"),
    ],
)
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
