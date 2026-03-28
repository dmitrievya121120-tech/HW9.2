from typing import Any, Dict, List


def filter_by_state(
    operations: List[Dict[str, Any]],
    state: str = "EXECUTED",
) -> List[Dict[str, Any]]:
    """
    Return list of operations with given state.

    :param operations: List of operation dictionaries.
    :param state: Required state value, default 'EXECUTED'.
    :return: New list with operations where 'state' == state.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(
    operations: List[Dict[str, Any]],
    reverse: bool = True,
) -> List[Dict[str, Any]]:
    """
    Return operations sorted by 'date' field.

    :param operations: List of operation dictionaries.
    :param reverse: Sort descending if True, ascending if False.
    :return: New sorted list.
    """
    return sorted(operations, key=lambda op: op.get("date", ""), reverse=reverse)
