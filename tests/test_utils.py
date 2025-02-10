from src.utils import financial_transactions


def test_financial_transactions_invalid() -> None:
    """Тест на отсутствие значения транзакции"""
    assert financial_transactions("") == []


def test_financial_transactions_empty() -> None:
    """Тест на отсутствие файла в директории или на его неправильное название"""
    assert financial_transactions("..//data/op.json") == []
