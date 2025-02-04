from typing import Any
from unittest.mock import patch

from src.external_api import getting_converted_currency


@patch("requests.get")
def test_getting_converted_currency(mock_get: Any) -> None:
    """Тест на правильность работы функции getting_converted_currency"""
    mock_get.return_value.json.return_value = {"rates": {"USD": 99.5}}
    assert getting_converted_currency("USD", 100.1) == 9747.14
