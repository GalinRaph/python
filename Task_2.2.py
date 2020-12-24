users_list = input('Введите элементы списка через пробел: ').split()
element_index = 0
for elem in range(int(len(users_list) / 2)):
    users_list[element_index], users_list[element_index + 1] = \
        users_list[element_index + 1], users_list[element_index]
    element_index = element_index + 2

print(users_list)
