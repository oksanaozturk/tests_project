import json


def get_data(filename: str) -> list:
    """
    Функцмя, получающая первоначальный список всех операций для фильтрации
    """
    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        return data


def get_filter_sorted_operations(data: list) -> list:
    """
    Функция, которая выбирает из списка выполненных операций только операции
    в статусе 'EXECUTED с дальнейшей сортировкой этого списка по дате, начиная с самой последней
    """
    operations_executed = []
    for operation in data:
        if 'state' in operation and operation['state'] == 'EXECUTED':
            operations_executed.append(operation)

    operations_sorted = sorted(operations_executed, key=lambda operation: operation['date'], reverse=True)
    return operations_sorted


def change_format_date(date: str) -> str:
    """
    Преобразовывает формат даты и времени в дату для пользователя.
    :param date: Дата и время операции (пример в формате '2019-08-26T10:50:58.294041').
    :return: Дата в формате ДД.ММ.ГГГГ (пример: 14.10.2018)
    """
    date = date.split('T')[0].split('-')
    return f'{date[2]}.{date[1]}.{date[0]}'


def change_account_or_card_format(data_of_numbers: str) -> str:
    """
    Функция, принимающая данные счета или карты и преобразующая их согласно условиям задачи:

    Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX
    (видны первые 6 цифр и последние 4,
    разбито по блокам по 4 цифры, разделенных пробелом).

    Номер счета замаскирован и не отображается целиком в формате  **XXXX
    (видны только последние 4 цифры номера счета).

    :param data_of_numbers: Номер счета в формате "Счет 64686473678894779589"
    или карты в формате "MasterCard 7158300734726758"

    :return: Номер карты в формате  XXXX XX** **** XXXX или Номер счета в формате  **XXXX
    """
    if "Счет" in data_of_numbers:
        num_chek = data_of_numbers.split(' ')[1]
        name_chek = data_of_numbers.split(' ')[0]
        return f"{name_chek} ** {num_chek[-4:]}"

    elif "Visa" in data_of_numbers:
        num_cart = data_of_numbers.split(' ')[-1]
        name_cart = data_of_numbers.split(' ')[0:-1]
        full_name_cart = " ".join(name_cart)
        return f"{full_name_cart} {num_cart[0:4]} {num_cart[5:7]}** **** {num_cart[-4:]}"

    else:
        num_cart = data_of_numbers.split(' ')[1]
        name_cart = data_of_numbers.split(' ')[0]
        return f"{name_cart} {num_cart[0:4] } {num_cart[5:7]}** **** {num_cart[-4:]}"
