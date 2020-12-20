usernumber = int(input('Поиск максимальной цифры в вашем числе:'))
array = []

while usernumber > 10:
    array.append(usernumber % 10)
    usernumber = usernumber // 10
maxarray = max(array)
print(maxarray)
