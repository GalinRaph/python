products = []
order = 1
name = None
price = None
quantity = None

while True:
    if name is None:
        value = input('Введите название товара: ')
        if not value.isalnum():
            print('Введите название товара:')
            continue

        name = value

    if price is None:
        value = input('Введите цену товара: ')
        if not value.isdigit():
            print('Введите цену товара: ')
            continue

        price = int(value)

    if quantity is None:
        value = input('Введите количество: ')
        if not value.isdigit():
            print('Введите количество: ')
            continue

        quantity = int(value)

    value = input('Введите единицы измерения: ')
    if not value.isalpha():
        print('Введите единицы измерения: ')
        continue

    unit = value

    products.append((
        order,
        {
            'Название': name,
            'Цена': price,
            'Количество': quantity,
            'ед': unit
        }
    ))

    name = None
    price = None
    quantity = None
    order = order + 1

    print(products)

    esc = input('Продолжить ввод? (да/нет) ')
    if esc.lower() == 'нет':
        break

analytics = {
    'Название': [],
    'Цена': [],
    'Количество': [],
    'ед': []
}

for element, item in products:
    analytics['Название'].append(item['Название'])
    analytics['Цена'].append(item['Цена'])
    analytics['Количество'].append(item['Количество'])
    analytics['ед'].append(item['ед'])

print(analytics)
