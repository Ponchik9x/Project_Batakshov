import pytest

from src.dict_reader import get_list_description_dict


@pytest.fixture
def list_dict() -> list[dict | dict]:
    return [
        {
            "id": 4361453.0,
            "state": "EXECUTED",
            "date": "2021-12-05T01:35:38Z",
            "amount": 30045.0,
            "currency_name": "Yuan Renminbi",
            "currency_code": "CNY",
            "from": "Mastercard 3665700271480451",
            "to": "American Express 0562165846839124",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 413942.0,
            "state": "EXECUTED",
            "date": "2023-01-14T17:09:31Z",
            "amount": 30885.0,
            "currency_name": "Zloty",
            "currency_code": "PLN",
            "from": "",
            "to": "Счет 14333875659976842245",
            "description": "Открытие вклада",
        },
        {
            "id": 3034414.0,
            "state": "EXECUTED",
            "date": "2020-05-17T04:31:24Z",
            "amount": 14490.0,
            "currency_name": "Rupiah",
            "currency_code": "IDR",
            "from": "Mastercard 5542284288235939",
            "to": "Discover 6909942117751005",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 595305.0,
            "state": "PENDING",
            "date": "2023-08-22T17:20:18Z",
            "amount": 22624.0,
            "currency_name": "Euro",
            "currency_code": "EUR",
            "from": "",
            "to": "Счет 97565556730475585217",
            "description": "Открытие вклада",
        },
    ]


def test_get_list_description_dict_valid(list_dict: list[dict | dict]) -> None:
    """Функция get_list_description_dict на правильность работы"""
    assert get_list_description_dict(list_dict, "Перевод") == [
        {
            "id": 4361453.0,
            "state": "EXECUTED",
            "date": "2021-12-05T01:35:38Z",
            "amount": 30045.0,
            "currency_name": "Yuan Renminbi",
            "currency_code": "CNY",
            "from": "Mastercard 3665700271480451",
            "to": "American Express 0562165846839124",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 3034414.0,
            "state": "EXECUTED",
            "date": "2020-05-17T04:31:24Z",
            "amount": 14490.0,
            "currency_name": "Rupiah",
            "currency_code": "IDR",
            "from": "Mastercard 5542284288235939",
            "to": "Discover 6909942117751005",
            "description": "Перевод с карты на карту",
        },
    ]


def test_get_list_description_nonelist(list_dict: list[dict | dict]) -> None:
    """Функция get_list_description_dict на правильность работы"""
    assert get_list_description_dict([], "Перевод") == []
