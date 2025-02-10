import re
from collections import Counter


def get_list_description_dict(list_dict: list[dict | dict], search_bar: str) -> list[dict]:
    """Функция принимает список словарей с данными
    о банковских операциях и строку поиска, и возвращает список словарей,
    у которых в описании есть данная строка.
    """
    search_bar_dict = []
    pattern = search_bar
    try:

        for diction in list_dict:

            if re.search(pattern, diction["description"]):
                search_bar_dict.append(diction)

    except ValueError:
        raise ValueError("Проверьте входящие данные")

    finally:
        return search_bar_dict


def counter_categories(list_dict: list[dict | dict], list_categories: list[str] | str) -> dict:
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    и возвращает словарь, в котором ключи — это названия категорий,
    и значения — это количество операций в каждой категории.
    """
    search_bar_dict = []

    try:

        for diction in list_dict:

            for cat in list_categories:
                pattern = cat

                if re.search(pattern, diction["description"]):
                    search_bar_dict.append(diction["description"])

    except ValueError:
        raise ValueError("Проверьте входящие данные")

    finally:
        return Counter(search_bar_dict)
