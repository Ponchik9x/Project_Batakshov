import pytest

from src.processing import filter_by_state


@pytest.fixture()
def state_dict() -> list[dict[str, str | int]]:
    """фикстура параметры state_dict"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_excluded(state_dict: list[dict[str, object]]) -> None:
    """Тест на правильность работы значение EXECUTED"""
    assert filter_by_state(state_dict, state="EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_canceled(state_dict: list[dict[str, object]]) -> None:
    """Тест на правильность работы значение CANCELED"""
    assert filter_by_state(state_dict, state="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_state_dict_zero_() -> None:
    """Тест на пустой список"""
    assert filter_by_state([]) == []


def test_filter_by_any_state(state_dict: list[dict[str, object]]) -> None:
    """Тест на правильность работы значение state=any"""
    assert filter_by_state(state_dict, state="any") == []


@pytest.fixture()
def not_state_dict() -> list[dict[str, str | int]]:
    """Фикстура state_dict без указания параметра state"""
    return [
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_not_state_(not_state_dict: list[dict[str, object]]) -> None:
    """Тест на правильность работы без указания параметра state(с помощью фикстуры)"""
    assert filter_by_state(not_state_dict, state="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
