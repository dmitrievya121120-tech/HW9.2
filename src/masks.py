def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает маску номера банковской карты.

    Args:
        card_number: Номер карты (целое число из 16 цифр)

    Returns:
        Маскированный номер карты в формате XXXX XX** **** XXXX
    """
    card_str = str(card_number)

    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    if not card_str.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")

    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Возвращает маску номера банковского счета.

    Args:
        account_number: Номер счета (целое число, минимум 4 цифры)

    Returns:
        Маскированный номер счета в формате **XXXX
    """
    account_str = str(account_number)

    if len(account_str) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    if not account_str.isdigit():
        raise ValueError("Номер счета должен содержать только цифры")

    return f"**{account_str[-4:]}"
