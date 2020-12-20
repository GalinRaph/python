pasttime = int(input('Сколько прошло секунд?'))
hourspassed = (pasttime//3600)
minutespassed = (pasttime//60)%60
secondspassed = (pasttime%60)
if hourspassed < 10:
    correctionfactor1 = 0
else:
    correctionfactor1 = ''
if minutespassed < 10:
    correctionfactor2 = 0
else:
    correctionfactor2 =''
if secondspassed < 10:
    correctionfactor3 = 0
else:
    correctionfactor3 = ''

print('Прошло времени:')
print(str(correctionfactor1) + str(hourspassed) + ':' + str(correctionfactor2) + str(minutespassed) + ':' + str(correctionfactor3) + str(secondspassed))
