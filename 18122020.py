# print('Hello world!')  # вывод на консоль
# Ctrl + / комментарий

# print(1 + 1)
# print(2 * 3)
# print(2 / 3)
# print(2 - 3)
# print(10 // 3)
# print(10 % 3)

# print(5**2)  # 5^2

# x_1 = 10
# x2 = 10
# print(x_1 + 1)
# print(x_1 + 10)
# 

# speed = 520
# print(speed)

# a = 'hello'
# a = 100
# print(a)


# str
# my_str = 'текст'
# print(my_str)
# print(type(my_str))

# int
# my_int = 50
# print(my_int)
# print(type(my_int))

# float
# my_float = 50.2
# print(my_float)
# print(type(my_float))

# bool
# my_bool = True  # False
# print(my_bool)
# print(type(my_bool))


# number = '5'
# print(number + str(5))
# print(int(number) + 5)


# user_answer = int(input('Введите число: '))
# print('Введено было', user_answer + 1)

# a = 4
# b = 5
# # print(a > b)
# # print(a < b)
# # print(a == b)
# # print(a != b)
# # print(a >= b)
# # print(a <= b)
# print(not(a > 0 and b < 0))
# print(not(a > 0 or b < 0))

# orig_pass = 'qwerty'
# admin_pass = 'admin'
#
# if input('Введите пароль: ') == orig_pass:
#     print('Авторизован успешно!')
#     print('Работа на сайте')
#     if input('Введите пароль админа: ') == admin_pass:
#         print('Даны права админа')
#     else:
#         print('Не даны права админа')
# else:
#     print('Пароль неверный!')


# color = 'фывфы'
#
# if color == 'red':
#     print('Красный')
# elif color == 'green':
#     print('Зеленый')
# elif color == 'blue':
#     print('Синий')
# else:
#     print('Неизвестный')

# number = int(input('Введите число меньше нуля: '))

# while True:
#     number = int(input('Введите число меньше нуля: '))
#     if number < 0:
#         break
#
# print('Справился')

# a = 1
# while a < 10:
#     a += 1  # a = a + 1
#     if a == 5:
#         continue
#     print(a)

CONSTANT = 54

name = 'Vlad'
age = 50
salary = 959595

print('Имя', name, 'Возраст', age, 'Зарплата', salary)
out_line = 'Имя %s Возраст %d Зарплата %d' % (name, age, salary)
print(out_line)
print('Имя {} Возраст {} Зарплата {}'.format(name, age, salary))

print(f'Имя {name} Возраст {age} Зарплата {salary}')
# print(f'{name=} {age=} {salary=}')

print(1, 2)


