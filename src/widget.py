import datetime

from src.masks import get_mask_card_number


def mask_account_card(card_name: str) -> str:
    """Функция возвращать строку с замаскированным номером.
    :param card_name: str:
    """
    type_of_card = card_name.rpartition(" ")[0]
    card_number = card_name.rpartition(" ")[-1]
    if len(card_number) > 16:
        return f"{type_of_card} {get_mask_card_number(card_number)}"
    elif len(card_number) == 16:
        return f"{type_of_card} {get_mask_card_number(card_number)}"
    else:
        raise ValueError("неверное значение")


def get_date(date_: str) -> str:
    """Функция возвращает строку с датой в формате "ДД.ММ.ГГГГ"("11.03.2024").
    :param date_: datetime:
    """
    split_date = date_.split("T")
    try:
        if date_:
            date_in_format = datetime.datetime.strptime(split_date[0], "%Y-%m-%d")
            date_string = date_in_format.strftime("%d-%m-%Y")
            return date_string
        else:
            raise ValueError("введите или проверьте дату")
    except ValueError:
        raise ValueError("неверный формат даты")


def get_lis_of_descriptions(list_transactions: list[dict | dict]) -> list[str]:
    """Функция получает лист с транзакциями и выдает лист с перечнем совершенных операций"""
    list_descriptions = []

    for diction in list_transactions:

        if diction["description"] not in list_descriptions:
            list_descriptions.append(diction["description"])

    return list_descriptions
