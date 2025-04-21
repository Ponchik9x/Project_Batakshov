from src.dict_reader import counter_categories, get_list_description_dict
from src.file_reader import read_file_csv, read_file_exel
from src.processing import filter_by_state, sort_by_date
from src.utils import financial_transactions
from src.widget import get_date, get_lis_of_descriptions, mask_account_card

print(
    """
Привет!
Добро пожаловать в программу работы с банковскими транзакциями.
"""
)
print(
    """
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
)

type_of_reading = str(input())

type_reading = ["1", "2", "3"]

while type_of_reading not in type_reading:
    print(f"чтение выбранного типа {type_of_reading} недоступно.")
    print(f"Введите тип из перечня: {", ".join(type_reading)}")
    type_of_reading = str(input())

user_list_transactions: list[dict | dict] = []

#                           ПРАВИЛЬНЫЙ КОД

# """__________________________________________________________"""
#                           ПРАВИЛЬНЫЙ КОД


if type_of_reading == "1":
    type_of_reading = ".json"
    print("Для обработки выбран JSON-файл.")
    name_of_transactions = f"data/operations{type_of_reading}"
    user_list_transactions = financial_transactions(name_of_transactions)

elif type_of_reading == "2":
    type_of_reading = ".csv"
    print("Для обработки выбран CSV-файл.")
    name_of_transactions = f"data/transactions{type_of_reading}"
    user_list_transactions = read_file_csv(name_of_transactions)

elif type_of_reading == "3":
    type_of_reading = ".xlsx"
    print("Для обработки выбран XLSX-файл.")
    name_of_transactions = f"data/transactions_excel{type_of_reading}"
    user_list_transactions = read_file_exel(name_of_transactions)


print(
    """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
)

states = ["EXECUTED", "CANCELED", "PENDING"]

state_filter = input().upper()

while state_filter not in states:
    print(f"Статус операции {state_filter} недоступен.")
    print(
        f"""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: {", ".join(states)}"""
    )
    state_filter = input().upper()

user_list_transactions = filter_by_state(user_list_transactions, state_filter)

print(f"Операции отфильтрованы по статусу {state_filter}")


yes_no_answer = ["да", "нет"]


print("Отсортировать операции по дате? Да/Нет")
sorted_by_date = input().lower()


while sorted_by_date not in yes_no_answer:
    print(f"Недопустимое значение: {sorted_by_date}.")
    print(f"Введите допустимое значение: {", ".join(yes_no_answer)}")
    sorted_by_date = input().lower()


if sorted_by_date == "да":
    print("Отсортировать по возрастанию или по убыванию? ")
    ascending_descending_order = input().lower()
    filter_ascending = ["по возрастанию", "по убыванию"]
    while ascending_descending_order not in filter_ascending:
        print(f"Недопустимое значение сортировки: {ascending_descending_order}.")
        print(f"Введите допустимое значение: {", ".join(filter_ascending)}")
        ascending_descending_order = input().lower()
    if sorted_by_date == "да" and ascending_descending_order == "по возрастанию":
        user_list_transactions = sort_by_date(user_list_transactions, reverse_list_dict=False)
    elif sorted_by_date == "да" and ascending_descending_order == "по убыванию":
        user_list_transactions = sort_by_date(user_list_transactions)
    else:
        user_list_transactions = user_list_transactions


print("Выводить только рублевые тразакции? Да/Нет")
transactions_in_rub = input().lower()


while transactions_in_rub not in yes_no_answer:
    print(f"Недопустимое значение: {transactions_in_rub}.")
    print(f"Введите допустимое значение: {", ".join(yes_no_answer)}")
    transactions_in_rub = input().lower()


print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
filter_by_description = input().lower()

while filter_by_description not in yes_no_answer:
    print(f"Недопустимое значение: {filter_by_description}.")
    print(f"Введите допустимое значение: {", ".join(yes_no_answer)}")
    filter_by_description = input().lower()

    if filter_by_description == "да":
        filter_word = input("Введите слово для фильтрации: ")
        if filter_by_description == "да":
            user_list_transactions = get_list_description_dict(user_list_transactions, filter_word)
            counter_operations = counter_categories(user_list_transactions, filter_word)
    else:
        user_list_transactions = user_list_transactions


if transactions_in_rub == "да":
    new_list_transactions = []
    for diction in user_list_transactions:
        if diction["currency_code"] == "RUB":
            new_list_transactions.append(diction)
    user_list_transactions = new_list_transactions
else:
    user_list_transactions = user_list_transactions


user_list_descriptions = get_lis_of_descriptions(user_list_transactions)

count_of_user_transactions = counter_categories(user_list_transactions, user_list_descriptions)

result_counter = 0
for k, v in count_of_user_transactions.items():
    result_counter += int(v)

print("Распечатываю итоговый список транзакций...")

print(f"Всего банковских операций в выборке: {result_counter}")

if len(user_list_transactions):
    for d in user_list_transactions:
        print(d["id"], d["state"], d["from"])

        if type(d["from"]) is str:
            df = str(d["from"]).split()
            print(
                f"""
            {get_date(d['date'])} {d['description']}
            {mask_account_card(d['from'])} -> {mask_account_card(d['to'])}
            Сумма: {d['amount']} {d['currency_code']}"""
            )

        else:
            print(
                f"""
            {get_date(d['date'])} {d['description']}
            {mask_account_card(d['to'])}
            Сумма: {d['amount']} {d['currency_code']}"""
            )
else:
    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
