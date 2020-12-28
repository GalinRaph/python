def comparison_func(array):
    max_number_1 = max(array)
    max_number_index = array.index(max(array))
    del array[max_number_index]
    max_number_2 = max(array)
    comparison = (int(max_number_1) + int(max_number_2))
    return comparison


users_list = input('Введите числа для получения суммы максимума через пробел: ').split()
users_list = [int(item) for item in users_list]
print('Сумма двух максимальных значений равна: ', comparison_func(users_list))


