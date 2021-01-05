from functools import reduce


def my_func(el_p, el):
    return el_p * el


even_array = [el for el in range(99, 1001) if el % 2 == 0]
print('Список четных значений: ', even_array)
print(f'Результат перемножения всех элементов списка: {reduce(my_func, even_array)}')
