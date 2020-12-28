def bio_func(name, surname, year_of_birth, living_city, email, phone):
    print('Вывожу ваши данные одной строкой: ', name, surname, ', родился в',
          year_of_birth, 'году, живёт в городе: ', living_city, 'Почта:',
          email, 'почта:', phone)


bio_func(name=input('Введите своё имя: '),
         surname=input('Введите свою фамилию: '),
         year_of_birth=input('Введите год своего рождения: '),
         living_city=input('Введите город своего проживания: '),
         email=input('Введите свою почту: '),
         phone=input('Введите свой номер телефона: '))

