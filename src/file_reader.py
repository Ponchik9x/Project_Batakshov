import csv

import pandas as pd


def read_file_csv(file_gate: str) -> list[dict[str, str]]:
    """Принимает на вход путь к файлу .csv и возвращает список словарей из файла"""
    return_list = []
    try:
        with open(file_gate) as csv_file:
            df = csv.DictReader(csv_file, delimiter=";")
            print(df)
            for row in df:
                return_list.append(row)
            return return_list

    except ValueError:
        return return_list


def read_file_exel(file_gate: str) -> list[dict[str, str]]:
    """Принимает на вход путь к файлу .exel и возвращает список словарей из файла"""
    returned_list = []
    try:
        df = pd.read_excel(file_gate)
        returned_list = df.to_dict(orient="records")
    finally:
        return returned_list
