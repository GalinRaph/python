print('Надеюсь,с вами учились ученики только с именем короче 10 символов.')
users_list = input('Введите имена ваших одноклассников через пробел: ').split()
i = 0
print('Получите список вашего класса:')
while i < len(users_list):
    print(str(i + 1), users_list[i][0:10])
    i = i + 1
    continue
