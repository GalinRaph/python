seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {12: 'Зима', 1: 'Зима', 2: 'Зима',
                3: 'Весна', 4: 'Весна', 5: 'Весна',
                6: 'Лето', 7: 'Лето', 8: 'Лето',
                9: 'Осень', 10: 'Осень', 11: 'ОСень'}
month_number = int(input("Введите номер месяца:"))
print(seasons_dict.get(month_number))
if month_number == 1 or month_number == 12 or month_number == 2:
    print(seasons_list[0])
if month_number == 3 or month_number == 4 or month_number == 5:
    print(seasons_list[1])
if month_number == 6 or month_number == 7 or month_number == 8:
    print(seasons_list[2])
if month_number == 9 or month_number == 10 or month_number == 11:
    print(seasons_list[3])


