from src.utils import (get_data, get_filter_sorted_operations, change_format_date,
                       change_account_or_card_format)


def test_get_data():
    """
    Функция проверяет, что при обработке json-файла мы что-то получаем
    """
    assert len(get_data('operations.json')) > 0


def test_get_filter_sorted_operations(test_operations_fixture):
    """
    Функцмя, которая получив из фикстуры информацию
    производит фильтрацию и сортировку
    :param test_operations_fixture:
    :return:None
    """
    assert len(get_filter_sorted_operations(test_operations_fixture)) == 5
    assert get_filter_sorted_operations(test_operations_fixture)[0]['date'] == '2023-01-26T15:40:13.413061'


def test_change_format_date(test_operations_fixture):
    """
    Функцмя, которая получив из фикстуры информацию,
    проверяет работу функции change_format_date
    :param test_operations_fixture:
    :return: None
    """
    assert change_format_date(get_filter_sorted_operations(test_operations_fixture)[0]['date']) == '26.01.2023'


def test_change_account_or_card_format(test_operations_fixture):
    """
    Функцмя, которая получив из фикстуры информацию,
    проверяет работу функции change_account_or_card_format
    :param test_operations_fixture:
    :return: None
    """
    assert (change_account_or_card_format(get_filter_sorted_operations(test_operations_fixture)[2]['from'])
            == 'Счет ** 8655')
    assert (change_account_or_card_format(get_filter_sorted_operations(test_operations_fixture)[3]['from'])
            == 'Visa Gold 5999 14** **** 6353')
    assert (change_account_or_card_format(get_filter_sorted_operations(test_operations_fixture)[0]['from'])
            == 'Maestro 4598 00** **** 4501')
