firstresult = int(input('Введите расстояние, которое вы пробежали в первый день (в км):'))
desiredresult = int(input('Введите желаемый результат при ежедневном десятипроцентном повышении расстояния (в км):'))
dayresult = 0
while desiredresult > firstresult:
    firstresult = firstresult * 1.1
    dayresult = dayresult + 1
print('На ' + str(dayresult) + '-й день вы пробежите не менее ' + str(desiredresult) + ' км')