from typing import Any
from unittest.mock import patch

from src.utils import financial_transactions, transaction_amount_dict


def test_financial_transactions_invalid() -> None:
    """Тест на отсутствие значения транзакции"""
    assert financial_transactions("") == []


def test_financial_transactions_empty() -> None:
    """Тест на отсутствие файла в директории или на его неправильное название"""
    assert financial_transactions("..//data/op.json") == []


@patch("requests.request")
def test_transaction_amount_dict(mock_get: Any = None) -> None:
    """Тест на правильность работы функции financial_transactions"""
    mock_get.return_value = {"operationAmount": {"amount": 1, "currency": {"code": "RUB"}}}
    assert transaction_amount_dict({"operationAmount": {"amount": 1, "currency": {"code": "RUB"}}}) == 1
