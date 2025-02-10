from src.decorators import log


def filter_by_state(state_dict: list[dict[str, object]], state: str = "EXECUTED") -> list[dict[str, object]]:
    """Функция возвращает список словарей по значению ключа "state" = EXECUTED"""
    filter_list = []
    for dict_ in state_dict:
        if dict_.get("state"):
            if dict_["state"] == state:
                filter_list.append(dict_)
        else:
            continue
    return filter_list


def sort_by_date(users_dict: list, reverse_list_dict: bool = True) -> list:
    """Функция сортирует список словарей по убыванию (reverse_list_dict = True)"""
    sort_by_date_dict = sorted(users_dict, key=lambda item: item["date"], reverse=reverse_list_dict)
    return sort_by_date_dict
