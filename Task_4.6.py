from itertools import count
from itertools import cycle


def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)


def my_cycle_func(my_list, iteration):
    i = 0
    iter_number = cycle(my_list)
    while i < iteration:
        print(next(iter_number))
        i = i + 1


my_count_func(start_number=int(input("Укажите число для генерации чисел: ")),
              stop_number=int(input("Укажите границу генерации чисел: ")))
my_cycle_func(my_list=[1, 2, 2, 4, 4, 6], iteration=int(input("Введите количество циклов: ")))
