def exponentiation_func(number, degree):
    result_2 = 1
    result_1 = 1 / (number ** degree)
    i = 1
    while degree > 0:
        result_2 = result_2 / number
        degree = degree - 1
    return result_1, result_2


users_number = float(input('Введите натуральное положительное число: '))
users_degree = int(input('Введите целое значение отрицательной степени: -'))
print(exponentiation_func(users_number, users_degree))
