import pytest

from src.masks import get_mask_card_number


@pytest.fixture()
def card_name() -> str:
    """Фикстура правильного номера карты"""
    return "1596837868705199"


def test_get_mask_card_number(card_name: str) -> None:
    """Тест на првильность работы"""
    assert get_mask_card_number(card_name) == "1596 83** **** 5199"


def test_get_mask_card_number_zero() -> None:
    """Тест на пустой ввод - ошибка"""
    with pytest.raises(ValueError):
        get_mask_card_number(card_num="")


def test_get_mask_card_number_below_len_card_num() -> None:
    """Тест на длинну ввода - ошибка (больше заданной)"""
    with pytest.raises(ValueError):
        get_mask_card_number(card_num="159683786870519912")


def test_get_mask_card_number_under_len_card_num() -> None:
    """Тест на длинну ввода - ошибка (меньше заданной)"""
    with pytest.raises(ValueError):
        get_mask_card_number(card_num="15968378687051")


@pytest.mark.parametrize(
    "account_number, expected",
    [("35383033474447895560", "**5560"), ("73654108430135874305", "**4305"), ("64686473678894779589", "**9589")],
)
def test_get_mask_account_write_input(account_number: str, expected: str) -> None:
    """Тест с параметрищацией на правильность ввода номера счета"""
    assert get_mask_card_number(account_number) == expected


def test_get_mask_account_number_zero() -> None:
    """Тест на пустой ввод номера счета - ошибка"""
    with pytest.raises(ValueError):
        get_mask_card_number(card_num="")


def test_get_mask_account_number_below_len_card_num() -> None:
    """Тест на заданную длину счета - ошибка (больше заданной)"""
    with pytest.raises(ValueError):
        get_mask_card_number(card_num="159683786870519912159848")


def test_get_mask_card_account_under_len_card_num() -> None:
    """Тест на заданную длинну счета - ошибка (мельше заданной)"""
    with pytest.raises(ValueError):
        get_mask_card_number(card_num="15968378687051")
