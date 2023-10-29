import json
from datetime import date


def get_data(filename: str) -> list:
    """Функцмя, получающая первоначальный список всех операций для фильтрации"""

    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        return data


def get_operations_executed(data) -> list:
    """
    Функция, которая выбирает из списка выполненных операций только операции
    в статусе 'EXECUTED
    """
    operations_executed = []
    for operation in data:
        if 'state' in operation and operation['state'] == 'EXECUTED':
            operations_executed.append(operation)
    return operations_executed


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
        return f"** {num_chek[-4:]}"
    else:
        num_cart = data_of_numbers.split(' ')[1]
        return f"{num_cart[0:5] } {num_cart[5:7]}** **** {num_cart[-4:]}"


if __name__ == '__main__':
    filename = 'operations.json'
    print(get_data(filename))
    print(get_operations_executed(get_data(filename)))
    print(len(get_data(filename)))
    print(len(get_operations_executed(get_data(filename))))
    print(change_format_date("2019-08-26T10:50:58.294041"))
    print(change_account_or_card_format("Счет 64686473678894779589"))
    print(change_account_or_card_format("MasterCard 7158300734726758"))

