import json
import logging
from json import JSONDecodeError
from typing import Any

from external_api import getting_converted_currency

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def financial_transactions(gate_to_transaction: str) -> list[dict[Any, Any] | dict[Any, Any]] | list:
    """
    Функция принимает путь к файлу JSON и возвращает список словарей,
    Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список.
    """
    logger.info(f"Принимаем путь к файлу JSON: {gate_to_transaction}")
    try:
        logger.info(f"Открываем файл JSON по адресу: {gate_to_transaction}")
        with open(f"{gate_to_transaction}") as file:

            try:
                content = json.load(file)
                if len(content) > 0 or tuple(content) == list:
                    logger.info(f"возвращаем список словарей из файла: {gate_to_transaction}")
                    return content

            except JSONDecodeError as ex:
                logger.error(f"Файл не формата JSON: {ex}")
                return []

    except FileNotFoundError as ex:
        logger.error(f"Файл не найден: {ex}")
        return []


def transaction_amount_dict(dict_of_transactions: dict) -> list[dict[Any, Any]] | Any:
    """
    Функция принимает на вход транзакцию и возвращает
    сумму транзакции (amount) в рублях, тип данных — float.
    Если сумма транзакции не в рублях, то происходит конвертация в рубли по настоящему курсу
    """
    try:
        logger.info(f"Получение значения суммы из входящего словаря: {dict_of_transactions}")
        amount = dict_of_transactions["operationAmount"]["amount"]

        logger.info(f"Получение значения валюты из входящего словаря: {dict_of_transactions}")
        type_currency = dict_of_transactions["operationAmount"]["currency"]["code"]

        if type_currency == "RUB":
            logger.info(f"Валюта - {type_currency}. Вывод значения")
            return amount
        else:
            logger.info(f"Валюта - {type_currency}. Конвертация суммы в RUB")
            return getting_converted_currency(dict_of_transactions)
    except ValueError:
        logger.error(f"Неверное значения или словарь не существует: {dict_of_transactions}")
        print("Проверьте входящее значение")
        return []
