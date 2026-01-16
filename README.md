# Виджет банковских операций

Проект для обработки списка банковских операций клиента: фильтрация по статусу и сортировка по дате.

## Установка

Клонируйте репозиторий и установите зависимости (если используются Poetry/requirements.txt).

```bash
git clone <URL_репозитория>
cd <папка_проекта>
python
from src.processing import filter_by_state, sort_by_date

operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

executed = filter_by_state(operations)                 # только EXECUTED
canceled = filter_by_state(operations, "CANCELED")     # только CANCELED

sorted_desc = sort_by_date(operations)                 # по убыванию даты
sorted_asc = sort_by_date(operations, reverse=False)   # по возрастанию