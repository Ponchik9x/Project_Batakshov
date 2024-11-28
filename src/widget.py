from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_name: str) -> str:
    """Функция возвращать строку с замаскированным номером."""
    type_of_card = card_name.rpartition(" ")[0]
    card_number = card_name.rpartition(" ")[-1]
    if len(card_number) > 16:
        return f"{type_of_card}{get_mask_account(card_number)}"
    elif len(card_number) == 16:
        return f"{type_of_card}{get_mask_card_number(card_number)}"
    else:
        return "неверное значение"


def get_date(datatime: datetime) -> str:
    """Функция возвращает строку с датой в формате "ДД.ММ.ГГГГ"("11.03.2024")."""
    current_time = datetime.now()
    formated_date = current_time.strftime("%d.%m.%Y")
    return formated_date
