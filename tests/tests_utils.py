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
    :return:
    """
    assert len(get_filter_sorted_operations(test_operations_fixture)) == 5
