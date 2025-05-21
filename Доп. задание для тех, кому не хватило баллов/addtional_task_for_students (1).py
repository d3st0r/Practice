# TODO Написать свою реализацию функции для подсчёта числа вхождение элементов в список
def my_count(l: list, item) -> int:
    count = 0  # Начальное значение счётчика

    # Перебираем все элементы списка
    for element in l:
        # Если текущий элемент равен искомому
        if element == item:
            count += 1  # Увеличиваем счётчик

    return count  # Возвращаем итоговый результат
some_kind_of_list = [1, 22, 10, 22, 1, 0, 3]
print(my_count(some_kind_of_list, 22))