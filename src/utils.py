import json
from json import JSONDecodeError
from typing import Any

from external_api import getting_converted_currency


def financial_transactions(gate_to_transaction: str) -> list[dict[Any, Any] | dict[Any, Any]] | list:
    """
    Функция принимает путь к файлу JSON и возвращает список словарей,
    Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список.
    """
    try:
        with open(f"{gate_to_transaction}") as file:

            try:
                content = json.load(file)
                if len(content) > 0 or tuple(content) == list:
                    return content

            except JSONDecodeError:
                return []

    except FileNotFoundError:
        return []


def transaction_amount_dict(dict_of_transactions: dict) -> list[dict[Any, Any]] | Any:
    """
    Функция принимает на вход транзакцию и возвращает
    сумму транзакции (amount) в рублях, тип данных — float.
    Если сумма транзакции не в рублях, то происходит конвертация в рубли по настоящему курсу
    """
    amount = dict_of_transactions["operationAmount"]["amount"]
    type_currency = dict_of_transactions["operationAmount"]["currency"]["code"]
    if type_currency == "RUB":
        return amount
    else:
        return getting_converted_currency(dict_of_transactions)
