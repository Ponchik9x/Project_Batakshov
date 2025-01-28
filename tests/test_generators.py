import pytest

from examples import transactions
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency() -> None:
    """Тест filter_by_currency() на правильность"""
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(generator) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


def test_filter_by_currency_zero_list() -> None:
    """Тест filter_by_currency() на отсутствие листа транзакций"""
    with pytest.raises(ValueError):
        filter_by_currency([], "USD")


def test_filter_by_zero_currency() -> None:
    """Тест filter_by_currency() на отсутствие ввода валюты"""
    with pytest.raises(ValueError):
        filter_by_currency(transactions, "")


def test_filter_by_invalid_currency() -> None:
    """Тест filter_by_currency() на правильность ввода валюты"""
    with pytest.raises(ValueError):
        filter_by_currency(transactions, "wer")


def test_transaction_descriptions() -> None:
    """Тест transaction_descriptions()  на правильность работы функции вывода описания"""
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


def test_transaction_zero_transactions_descriptions() -> None:
    """Тест transaction_descriptions() на отсутствие списка транзакций"""
    with pytest.raises(ValueError):
        list(transaction_descriptions([]))


def test_card_number_generator() -> None:
    """Тест card_number_generator() на правильность"""
    generator = card_number_generator(1, 4)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"


def test_card_number_generator_invalid_stop() -> None:
    """Тест card_number_generator() некорректный предел функции больше возможного"""
    with pytest.raises(ValueError):
        list(card_number_generator(1, 100000000000000021))


def test_card_number_generator_zero_stop() -> None:
    """Тест card_number_generator() некорректный предел функции меньше возможного"""
    with pytest.raises(ValueError):
        list(card_number_generator(1, 0))


def test_card_number_generator_invalid_start_below_stop() -> None:
    """Тест card_number_generator() некорректный предел функции старт больше стопа"""
    with pytest.raises(ValueError):
        list(card_number_generator(100000000000000021, 10))
