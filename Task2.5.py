my_list = [7, 5, 3, 3, 2]
count = 0
user_number = int(input('Введите вашу цифру для сравнения её со списком [7, 5, 3, 3, 2]: '))
if int(user_number) > 9:
    user_number = int(input('Вы ввели число! Введите цифру: '))

while count < len(my_list):
    if user_number < my_list[-1]:
        my_list.append(user_number)
        break
    elif user_number < my_list[count]:
        count = count + 1
        continue
    elif user_number > my_list[count]:
        my_list.insert(count, int(user_number))
        break
    else:
        break

print(my_list)
