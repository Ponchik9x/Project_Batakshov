# Работа над виджетом банковских операций клиента. 

## Использовуем Git для сохранения истории развития проекта.

    Создан локальный Git-репозиторий.
    Файл создан в корне проекта, в файле .gitignore учтена папка .idea
    В репозитории есть 3 или более коммита.
    В коммиты не добавлены игнорируемые файлы.

### Функции

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

#### функция sort_by_date
    принимает список словарей и необязательный параметр, 
    задающий порядок сортировки (по умолчанию — убывание)
    возвращает новый список, отсортированный по дате

## Примеры работы функций

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

