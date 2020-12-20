usernumber = int(input('Введите число n для вычисления функции вида "n+nn+nnn":'))
functionsum = usernumber + int(str(usernumber)+str(usernumber)) + int(str(usernumber)+str(usernumber)+str(usernumber))
print(str(functionsum))