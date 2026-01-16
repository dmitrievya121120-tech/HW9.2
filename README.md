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
