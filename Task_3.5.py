def my_sum():
    sum_result = 0
    esc = False
    while not esc:
        number = input('Введите последовательность чисел для суммирования: ').split()
        result = 0
        for element in range(len(number)):
            if number[element].lower() == 'стоп':
                esc = True
                break
            else:
                result = result + int(number[element])
        sum_result = sum_result + result
        print(f'Полученная сумма {sum_result}')


print('Введите "стоп" без кавычек для завершения')
my_sum()
