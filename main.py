from src.masks import get_mask_account, get_mask_card_number


def main() -> None:
    """Основная функция для демонстрации работы."""
    print("=" * 60)
    print("Демонстрация работы функций маскировки банковских данных")
    print("=" * 60)

    print("\n1. Маскировка номеров карт:")
    test_cards = [7000792289606361, 1234567812345678, 5555555555554444]

    for card in test_cards:
        masked = get_mask_card_number(card)
        print(f"   Карта: {card} -> {masked}")

    print("\n2. Маскировка номеров счетов:")
    test_accounts = [73654108430135874305, 123456789012, 98765432109876543210]

    for account in test_accounts:
        masked = get_mask_account(account)
        print(f"   Счет: {account} -> {masked}")

    print("\n" + "=" * 60)
    print("Тестирование завершено успешно!")
    print("=" * 60)


if __name__ == "__main__":
    main()
