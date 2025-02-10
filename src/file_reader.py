import pandas as pd


def read_file_csv(file_gate: str) -> list[dict[str, str]]:
    """Принимает на вход путь к файлу .csv и возвращает список словарей из файла"""
    return_list = []
    try:
        with open(file_gate, newline='') as csv_file:
            df = pd.read_csv(csv_file, delimiter=";")
            df = df.loc[df.id.notnull()]
            return_list = df.to_dict('records')
            return return_list

    except ValueError:
        return return_list


def read_file_exel(file_gate: str) -> list[dict[str, str]]:
    """Принимает на вход путь к файлу .exel и возвращает список словарей из файла"""
    returned_list = []
    try:
        df = pd.read_excel(file_gate)
        df = df.loc[df.id.notnull()]
        returned_list = df.to_dict(orient="records")
    except ValueError:
        print('Неверный адрес')
    finally:
        return returned_list
