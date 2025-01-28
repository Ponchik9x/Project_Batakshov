import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")


def getting_converted_currency(dict_transaction: dict) -> float:
    """Функция запрашивает настоящий курс стоимости валюты
    и конвертирует сумму операции в рубли"""

    amount = dict_transaction["operationAmount"]["amount"]
    type_currency = dict_transaction["operationAmount"]["currency"]["code"]

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={type_currency}&amount={amount}"

    payload = {}

    headers = {"apikey": f'{os.getenv("API_LAYER_KEY")}'}

    response = requests.request("GET", url, headers=headers, data=payload)

    result = response.json()

    return result["result"]  # round(converted_operation, 2)
