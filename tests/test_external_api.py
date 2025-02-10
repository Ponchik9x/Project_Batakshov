from typing import Any
from unittest.mock import patch

from src.external_api import transaction_amount_dict

#
# @patch('requests.get')
# def test_get_github_user_info(mock_get):
#     mock_get.return_value.json.return_value = {'login': 'testuser', 'name': 'Test User'}
#     assert get_github_user_info('testuser') == {'login': 'testuser', 'name': 'Test User'}


@patch("requests.request")
def test_getting_converted_currency(mock_get: Any) -> None:
    """Тест на правильность работы функции getting_converted_currency"""
    mock_get.return_value.json.return_value = {
        "date": "2018-02-22",
        "historical": "",
        "info": {"rate": 148.972231, "timestamp": 1519328414},
        "query": {"amount": 25, "from": "GBP", "to": "JPY"},
        "result": 3724.305775,
        "success": True,
    }
    assert (
        transaction_amount_dict(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "usd", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        == 3724.305775
    )


@patch("requests.request")
def test_transaction_amount_dict(mock_get: Any = None) -> None:
    """Тест на правильность работы функции financial_transactions"""
    mock_get.return_value = {"operationAmount": {"amount": 1, "currency": {"code": "RUB"}}}
    assert transaction_amount_dict({"operationAmount": {"amount": 1, "currency": {"code": "RUB"}}}) == 1
