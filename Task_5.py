proceeds = int(input('Введите годовую выручку вашего предприятия в рублях:'))
outplay = int(input('Введите значение годовых издержек вашего предприятия в рублях:'))
profit = int(proceeds - outplay)
rent = int(profit * 100 / proceeds)

if proceeds > outplay:
    print('Ваше предприятие рентабельно! Чистая прибыль: ' + str(proceeds - outplay))
    print('Ваша рентабельность составляет ' + str(rent) + '%')
else:
    print('Ваше предприятие подлежит к банкротству!')
personnel = int(input('Введите количество персонала:'))
personrent = int(profit / personnel)
print('Прибыль вашей фирмы на одного сотрудника составляет ' + str(personrent) + ' рубль')