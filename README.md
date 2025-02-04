> # Работа над виджетом банковских операций клиента. 

> ## Используем Git для сохранения истории развития проекта.

    Создан локальный Git-репозиторий.
    Файл создан в корне проекта, в файле .gitignore учтена папка .idea
    В репозитории есть 3 или более коммита.
    В коммиты не добавлены игнорируемые файлы.

> ### Функции

#### Функция get_mask_card_number и get_mask_account из модуля masks
    принимает на вход строку и возвращает зашифрованные данные пользователя

#### Функция get_date из модуля widget
    принимает на вход строку и отдает корректный результат в формате:
    11.07.2018  ДД.ММ.ГГГГ

#### Функция mask_account_card из модуля widget
    принимает название карты и ее номер или название счета и его номер 
    и возвращает название и зашиврованный номер карты или счета

#### Функция filter_by_state из модуля processing 
    принимает список словарей и опционально значение для ключа('EXECUTED')
    возвращает новый список словарей, содержащий только те словари,
    у которых ключ соответствует заданному

#### Функция sort_by_date
    принимает список словарей и необязательный параметр, 
    задающий порядок сортировки (по умолчанию — убывание)
    возвращает новый список, отсортированный по дате
    
#### Функция filter_by_currency 
    возвращает итератор, который поочередно выдает транзакции, где валюта операции
    соответствует заданной

#### Функция transaction_descriptions 
    принимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди

#### Функция-генератор card_number_generator 
    выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    X — цифра номера карты, диапазон от 0000 0000 0000 0001 до 9999 9999 9999 9999"
    
#### Декоратор-функция log
    Декоратор-функция автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
    Декоратор принимает необязательный аргумент filename, который определяет, куда будут записываться логи (в файл или в консоль):
    Если filename задан, логи записываются в указанный файл.
    Если filename не задан, логи выводятся в консоль.

#### Функция financial_transactions
    Функция принимает путь к файлу JSON и возвращает список словарей,
    Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список.    

#### Функция transaction_amount_dict
    Функция принимает на вход транзакцию и возвращает
    сумму транзакции (amount) в рублях, тип данных — float.
    Если сумма транзакции не в рублях, то происходит конвертация в рубли по настоящему курсу

#### Функция getting_converted_currency
    Функция запрашивает настоящий курс стоимости валюты
    и конвертирует сумму операции в рубли


> ## Примеры работы функций

    # Пример для карты
    Visa Platinum 7000792289606361  # входной аргумент
    Visa Platinum 7000 79** **** 6361  # выход функции

    # Пример для счета
    "Счет 73654108430135874305"  # входной аргумент
    Счет **4305  # выход функции

    # функция get_date 
    "2024-03-11T02:26:18.671407" # входной аргумент
    11.03.2024 # выход функции

    # Примеры работы функции filter_by_state
    Выход функции со статусом по умолчанию 'EXECUTED'
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    Выход функции, если вторым аргументов передано 'CANCELED'
    [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

    # Примеры работы функции sort_by_date
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    
    # Примеры работы функции filter_by_currency

    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(2):
    print(next(usd_transactions))
    {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
    }

    # Примеры работы функции transaction_descriptions
    
    descriptions = transaction_descriptions(transactions)
    for _ in range(5):
    print(next(descriptions))

    Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации

    # Примеры работы функции card_number_generator

    for card_number in card_number_generator(1, 5):
    print(card_number)

    0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
    
    # Примеры работы декоратор-функции log
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y
    --------------
    my_function(1, 2)
    Ожидаемый вывод в лог-файл
    mylog.txt
    при успешном выполнении:
    my_function ok
    Ожидаемый вывод при ошибке:
    my_function error: тип ошибки. Inputs: (1, 2), {}
    Где тип ошибки заменяется на текст ошибки.

    


#### Примеры входных данных для проверки функции
   
    ---
    Maestro 1596837868705199
    Счет 64686473678894779589
    MasterCard 7158300734726758
    Счет 35383033474447895560
    Visa Classic 6831982476737658
    Visa Platinum 8990922113665229
    Visa Gold 5999414228426353
    Счет 73654108430135874305
    ---
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    ---
    transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }])

> # Раздел тестов 


> ## Работа теста для модуля masks
### FUNCTIONS test_masks

    card_name() -> str
        Фикстура правильного номера карты

    test_get_mask_account_number_below_len_card_num() -> None
        Тест на заданную длину счета - ошибка (больше заданной)

    test_get_mask_account_number_zero() -> None
        Тест на пустой ввод номера счета - ошибка

    test_get_mask_account_write_input(account_number: str, expected: str) -> None
        Тест с параметрищацией на правильность ввода номера счета

    test_get_mask_card_account_under_len_card_num() -> None
        Тест на заданную длинну счета - ошибка (мельше заданной)

    test_get_mask_card_number(card_name: str) -> None
        Тест на првильность работы

    test_get_mask_card_number_below_len_card_num() -> None
        Тест на длинну ввода - ошибка (больше заданной)

    test_get_mask_card_number_under_len_card_num() -> None
        Тест на длинну ввода - ошибка (меньше заданной)

    test_get_mask_card_number_zero() -> None
        Тест на пустой ввод - ошибка


> ## Работа теста для модуля processing
### FUNCTIONS test_processingq

    not_state_dict() -> list[dict[str, str | int]]
        Фикстура state_dict без указания параметра state

    state_dict() -> list[dict[str, str | int]]
        Фикстура параметры state_dict

    test_filter_by_any_state(state_dict: list[dict[str, object]]) -> None
        Тест на правильность работы значение state=any

    test_filter_by_not_state_(not_state_dict: list[dict[str, object]]) -> None
        Тест на правильность работы без указания параметра state(с помощью фикстуры)

    test_filter_by_state_canceled(state_dict: list[dict[str, object]]) -> None
        Тест на правильность работы значение CANCELED

    test_filter_by_state_excluded(state_dict: list[dict[str, object]]) -> None
        Тест на правильность работы значение EXECUTED

    test_filter_by_state_state_dict_zero_() -> None
        Тест на пустой список


> ## Работа теста для модуля widget
### FUNCTIONS test_widget

    test_get_date_invalid() -> None
        Тест на пустой ввод даты - ошибка

    test_get_date_zero() -> None
        Тест на пустой ввод даты - ошибка

    test_mask_account_card_number_below_len_card_num() -> None
        Тест на заданную длинну счета - ошибка (мельше заданной)

    test_mask_account_card_number_under_len_card_name(card_name: str, exception: Any) -> None
        Тест на заданную длину счета - ошибка (больше заданной)
        :param card_name: str
        :param exception: typing.Any

    test_mask_account_card_write_input(card_name: str, expected: str) -> None
        Тест с параметризацией на правильность работы функции
        :param card_name: str:
        :param expected: str:

    test_mask_account_card_zero() -> None
        Тест на пустой ввод номера счета - ошибка


> ## Работа теста для модуля generators
### FUNCTIONS test_generators


    test_filter_by_currency() -> None
        Тест filter_by_currency() на правильность

    test_filter_by_currency_zero_list() -> None
        Тест filter_by_currency() на отсутствие листа транзакций

    test_filter_by_zero_currency() -> None
        Тест filter_by_currency() на отсутствие ввода валюты

    test_filter_by_invalid_currency() -> None
        Тест filter_by_currency() на правильность ввода валюты 
    
    test_transaction_descriptions() -> None
        Тест transaction_descriptions()  на правильность работы функции вывода описания

    test_transaction_zero_transactions_descriptions() -> None
        Тест transaction_descriptions() на отсутствие списка транзакций

    test_card_number_generator()
        Тест card_number_generator() на правильность

    test_card_number_generator_invalid_stop()
        Тест card_number_generator() некорректный предел функции больше возможного

    test_card_number_generator_zero_stop()
        Тест card_number_generator() некорректный предел функции меньше возможного

    test_card_number_generator_invalid_start_below_stop()
        Тест card_number_generator() некорректный предел функции старт больше стопа


# Раздел тестов 


## Работа теста для модуля masks
### FUNCTIONS test_masks

    card_name() -> str
        Фикстура правильного номера карты

    test_get_mask_account_number_below_len_card_num() -> None
        Тест на заданную длину счета - ошибка (больше заданной)

    test_get_mask_account_number_zero() -> None
        Тест на пустой ввод номера счета - ошибка

    test_get_mask_account_write_input(account_number: str, expected: str) -> None
        Тест с параметрищацией на правильность ввода номера счета

    test_get_mask_card_account_under_len_card_num() -> None
        Тест на заданную длинну счета - ошибка (мельше заданной)

    test_get_mask_card_number(card_name: str) -> None
        Тест на првильность работы

    test_get_mask_card_number_below_len_card_num() -> None
        Тест на длинну ввода - ошибка (больше заданной)

    test_get_mask_card_number_under_len_card_num() -> None
        Тест на длинну ввода - ошибка (меньше заданной)

    test_get_mask_card_number_zero() -> None
        Тест на пустой ввод - ошибка


## Работа теста для модуля processing
### FUNCTIONS test_processingq

    not_state_dict() -> list[dict[str, str | int]]
        Фикстура state_dict без указания параметра state

    state_dict() -> list[dict[str, str | int]]
        Фикстура параметры state_dict

    test_filter_by_any_state(state_dict: list[dict[str, object]]) -> None
        Тест на правильность работы значение state=any

    test_filter_by_not_state_(not_state_dict: list[dict[str, object]]) -> None
        Тест на правильность работы без указания параметра state(с помощью фикстуры)

    test_filter_by_state_canceled(state_dict: list[dict[str, object]]) -> None
        Тест на правильность работы значение CANCELED

    test_filter_by_state_excluded(state_dict: list[dict[str, object]]) -> None
        Тест на правильность работы значение EXECUTED

    test_filter_by_state_state_dict_zero_() -> None
        Тест на пустой список


## Работа теста для модуля widget
### FUNCTIONS test_widget

    test_get_date_invalid() -> None
        Тест на пустой ввод даты - ошибка

    test_get_date_zero() -> None
        Тест на пустой ввод даты - ошибка

    test_mask_account_card_number_below_len_card_num() -> None
        Тест на заданную длинну счета - ошибка (мельше заданной)

    test_mask_account_card_number_under_len_card_name(card_name: str, exception: Any) -> None
        Тест на заданную длину счета - ошибка (больше заданной)
        :param card_name: str
        :param exception: typing.Any

    test_mask_account_card_write_input(card_name: str, expected: str) -> None
        Тест с параметризацией на правильность работы функции
        :param card_name: str:
        :param expected: str:

    test_mask_account_card_zero() -> None
        Тест на пустой ввод номера счета - ошибка


## Работа теста для модуля decorators
### FUNCTIONS test_decorators

    test_log():
        Тест на проверку правильности работы декоратора без добавления в модуль для логов

    test_log_filename():
        Тест на проверку правильности работы декоратора добавлением в определенный модуль для логов


## Работа теста для модуля utils
### FUNCTIONS tests.test_utils

    test_financial_transactions_empty()
        Тест на отсутствие файла в директории или на его неправильное название

    test_financial_transactions_invalid()
        Тест на отсутствие значения транзакции

    test_transaction_amount_dict(mock_get=None)
        Тест на правильность работы функции financial_transactions


## Работа теста для модуля external_api
### FUNCTIONS tests.test_external_api

    test_getting_converted_currency(mock_get)
        Тест на правильность работы функции getting_converted_currency


