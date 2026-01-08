"""Widget модуль для работы с картами и счетами."""

from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


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
    parts: list[str] = card_info.split()

    if parts[0] == "Счет":
        card_type: str = "Счет"
        number_str: str = parts[1]
        number: int = int(number_str)
        masked_number: str = get_mask_account(number)
    else:
        # Для карт (Visa, Maestro, MasterCard и т.д.)
        card_type = " ".join(parts[:-1])
        number_str = parts[-1]
        number = int(number_str)
        masked_number = get_mask_card_number(number)

    return f"{card_type} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует ISO формат даты в формат ДД.ММ.ГГГГ.

    :param date_string: Строка с датой в формате "2024-03-11T02:26:18.671407"
    :return: Дата в формате "11.03.2024"
    """
    dt: datetime = datetime.fromisoformat(date_string)
    return dt.strftime("%d.%m.%Y")
