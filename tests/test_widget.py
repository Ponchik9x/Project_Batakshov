import typing

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_name, expected",
    [
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_mask_account_card_write_input(card_name: str, expected: str) -> None:
    """Тест с параметризацией на правильность работы функции
    :param card_name: str:
    :param expected: str:
    """
    assert mask_account_card(card_name) == expected


def test_mask_account_card_zero() -> None:
    """Тест на пустой ввод номера счета - ошибка"""
    with pytest.raises(ValueError):
        mask_account_card(card_name="")


@pytest.mark.parametrize(
    "card_name, exception",
    [
        ("Счет 159683786870519912159848", pytest.raises(ValueError)),
        ("Visa Platinum 8990922113665229222", pytest.raises(ValueError)),
        ("MasterCard 7158300734726758333", pytest.raises(ValueError)),
    ],
)
def test_mask_account_card_number_under_len_card_name(card_name: str, exception: typing.Any) -> None:
    """Тест на заданную длину счета - ошибка (больше заданной)
    :param card_name: str
    :param exception: typing.Any
    """
    with exception as e:
        assert mask_account_card(card_name) == e


def test_mask_account_card_number_below_len_card_num() -> None:
    """Тест на заданную длинну счета - ошибка (мельше заданной)"""
    with pytest.raises(ValueError):
        mask_account_card(card_name="Счет 15968378687051")
        mask_account_card(card_name="Visa Platinum 899092211366522")
        mask_account_card(card_name="MasterCard 7158300734726758333")


def test_get_date_zero() -> None:
    """Тест на пустой ввод даты - ошибка"""
    with pytest.raises(ValueError):
        get_date("")
