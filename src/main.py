from src.utils import (get_data, get_filter_sorted_operations, change_format_date,
                       change_account_or_card_format)


def main():
    # Получение отфильтрованного и отсортированного списка операцийиз файла operations.json
    filename = 'operations.json'
    operations_sorted = get_filter_sorted_operations(get_data(filename))

    # Получение последних пяти операций
    # operations_last_five = operations_with_from[0:5]
    operations_last_five = operations_sorted[0:5]

    # Вызов данных по операции в требуемом формате
    # 14.10.2018 Перевод организации
    # Visa Platinum 7000 79 ** ** ** 6361 -> Счет ** 9638
    # 82771.72 руб.
    for operation in operations_last_five:
        date = change_format_date(operation['date'])
        print(f"{date} {operation['description']}")

        # Создание условия для вывода данных по операциям, у которых отсутвует ключ "from" и с ключом
        if 'from' not in operation:
            num_from = None
        else:
            num_from = change_account_or_card_format(operation['from'])
        num_to = change_account_or_card_format(operation['to'])
        print(f"{num_from} -> {num_to}")
        print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}")
        print()


if __name__ == "__main__":
    main()
