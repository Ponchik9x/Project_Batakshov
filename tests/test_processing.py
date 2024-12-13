import pytest

from src.processing import filter_by_state


@pytest.fixture()
def state_dict() -> list[dict[str, str | int]]:
    """параметры state_dict"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_excluded(state_dict: list[dict[str, object]]) -> None:
    """Тест на правильность работы"""
    assert filter_by_state(state_dict, state="EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_canceled(state_dict: list[dict[str, object]]) -> None:
    """Тест на правильность работы"""
    assert filter_by_state(state_dict, state="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_state_dict_zero_() -> None:
    """Тест на пустой список"""
    assert filter_by_state([]) == []
