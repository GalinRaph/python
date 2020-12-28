def division_func(dividend, divider):
    try:
        division = dividend / divider
    except ZeroDivisionError:
        return 'Вы ввели недопустимое значение!'
    return division


users_dividend = int(input('Введите делимое: '))
users_divider = int(input('Введите делитель: '))
answer = division_func(users_dividend, users_divider)
print('Результат деления: ', answer)

