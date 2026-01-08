"""Widget модуль для работы с картами и счетами."""

from datetime import datetime

from src.masks import mask_account
from src.masks import mask_card


def mask_account_card(card_info: str) -> str:
    """
    Маскирует номер карты или счета, сохраняя информацию о типе.

    Функция обрабатывает строки следующих форматов:
    - Visa Platinum 7000792289606361
    - Maestro 7000792289606361
    - Счет 73654108430135874305

    :param card_info: Строка с информацией о карте или счете
    :return: Строка с замаскированным номером и типом
    """
    parts: list[str] = card_info.split(" ", 1)
    card_type: str = parts
    number: str = parts

    if card_type == "Счет":
        masked_number: str = mask_account(number)
    else:
        masked_number: str = mask_card(number)

    return f"{card_type} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует ISO формат даты в формат ДД.ММ.ГГГГ.

    :param date_string: Строка с датой в формате "2024-03-11T02:26:18.671407"
    :return: Дата в формате "11.03.2024"
    """
    dt: datetime = datetime.fromisoformat(date_string)
    return dt.strftime("%d.%m.%Y")
