import logging
import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv(".env")

logger = logging.getLogger("external_api")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/external_api.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


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

            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={type_currency}&amount={amount}"

            payload: dict = {}

            headers = {"apikey": f'{os.getenv("API_LAYER_KEY")}'}

            response = requests.request("GET", url, headers=headers, data=payload)

            result = response.json()
            return result["result"]

    except ValueError:
        logger.error(f"Неверное значения или словарь не существует: {dict_of_transactions}")
        print("Проверьте входящее значение")
        return []
