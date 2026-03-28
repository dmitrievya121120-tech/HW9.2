from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default():
    operations = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
    ]

    result = filter_by_state(operations)

    assert len(result) == 2
    assert all(op["state"] == "EXECUTED" for op in result)
import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
    ]


def test_filter_by_state_default(sample_operations):
    result = filter_by_state(sample_operations)

    assert len(result) == 2
    assert all(op["state"] == "EXECUTED" for op in result)
@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3]),
        ("CANCELED", [2]),
        ("PENDING", []),
    ],
)
def test_filter_by_state_param(sample_operations, state, expected_ids):
    result = filter_by_state(sample_operations, state=state)
    ids = [op["id"] for op in result]

    assert ids == expected_ids
def test_sort_by_date_desc(sample_operations):
    result = sort_by_date(sample_operations)

    dates = [op["date"] for op in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_asc(sample_operations):
    result = sort_by_date(sample_operations, reverse=False)

    dates = [op["date"] for op in result]
    assert dates == sorted(dates)
