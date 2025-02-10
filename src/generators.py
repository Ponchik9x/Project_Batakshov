from typing import Any, Generator


def filter_by_currency(
    list_of_transactions: list[dict[str | int, dict[str, dict[Any, Any]]]], currency: str
) -> Generator[dict[str | int, dict[str, dict[Any, Any]]], Any, None]:
    """Функция filter_by_currency возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    if len(list_of_transactions) == 0 or len(currency) == 0:
        raise ValueError("Проверьте данные на входе")
    for v in list_of_transactions:
        if v["operationAmount"]["currency"]["code"] == currency:
            dict_of_currency = (
                item for item in list_of_transactions if item["operationAmount"]["currency"]["code"] == currency
            )
            return dict_of_currency
        else:
            raise ValueError("Операции с такой валютой не производились или указана неверная валюта")


def transaction_descriptions(list_of_transactions):
    """
    Функция transaction_descriptions принимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди
    """
    if len(list_of_transactions) <= 0:
        raise ValueError("Проверьте данные на входе")
    else:
        for item in list_of_transactions:
            string_descriptions = item["description"]
            yield string_descriptions


def card_number_generator(start, stop):
    """Функция-генератор card_number_generator выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    X — цифра номера карты, диапазон от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    if stop >= 10000000000000000 or stop <= 0:
        raise ValueError("некорректный предел карты")
    elif start < 0 or stop < 0:
        raise ValueError("некорректный ввод данных")
    elif start >= stop:
        raise ValueError("начальное значение больше или равно конечного")
    else:
        for n in range(start, stop):
            zero_for_card = 16 - len(str(n))
            card_num = "0" * zero_for_card + str(n)
            card_num_split = f"{str(card_num)[:4]} {str(card_num[4:8])} {str(card_num[8:12])} {str(card_num[-4:])}"
            yield card_num_split
