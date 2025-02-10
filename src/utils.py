import json
import logging
from json import JSONDecodeError
from typing import Any



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
