# Python Project 1
## Learning Python with Poetry
## decorators

Модуль `decorators` содержит декоратор `log`, который логирует результат работы функции или ошибку.

Пример использования (лог в консоль):

```python
from src.decorators import log

@log()
def add(a, b):
    return a + b
## generators

Модуль `generators` содержит:

- `filter_by_currency(transactions, currency)` — генератор операций с нужной валютой.
- `transaction_descriptions(transactions)` — генератор описаний операций.
- `card_number_generator(start, count)` — генератор номеров карт в формате `XXXX XXXX XXXX XXXX`.

Пример:

```python
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)

# фильтрация по валюте
for tx in filter_by_currency(transactions, "USD"):
    print(tx)

# только описания
for desc in transaction_descriptions(transactions):
    print(desc)

# генерация номеров карт
for num in card_number_generator(1, 3):
    print(num)
## Тестирование

Для запуска тестов:

```bash
pytest
