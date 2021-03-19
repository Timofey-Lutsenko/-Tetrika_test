# В условиях задания массив, а в примере вызова вункции строка, в связи с этим
# в генераторе массива использовал преобразование строки в массив.
from random import randrange


# Генерация входящего массива единиц и нулей в
# функцию поиска индекса первого нуля.
# O(len(num_of_one + num_of_zero))
def arr_gen(num_of_one, num_of_zero):
    temp_str = '1' * num_of_one + '0' * num_of_zero
    print(temp_str)
    return list(temp_str)


# Функция поиска индекса первого нуля в массиве, на базе метода .index()
# O(1)
def first_zero_index(task_array):
    return task_array.index('0')


# Функция посика индекса первого нуля в массиве на базе цикла.
# Сложность O(n)
def first_zero_cycle(task_array):
    try:
        i = 0
        for el in task_array:
            if el == '0':
                return i
            i += 1
    except ValueError:
        return 'Incorrect value.'
    except TypeError:
        return 'Incorrect type.'


# Функция поиска индекса первого нуля в массиве на базе подсчета кол-ва единиц.
# Сложность O(n)
def first_zero_count(task_array):
    return task_array.count('1')


# Вызов функции генерации списка с случайным кол-ом значений из диапазона.
some_arr = arr_gen(
    randrange(1, 10),
    randrange(1, 10)
)

# Вызовы функций поиска индекса.
# Втроенным методом.
print(first_zero_index(some_arr))
# Циклом.
print(first_zero_cycle(some_arr))
# Подсчетом единиц.
print(first_zero_count(some_arr))
