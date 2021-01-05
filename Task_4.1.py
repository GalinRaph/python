from sys import argv


def calculation():
    script_name, production, salary, premium = argv
    production = int(production)
    salary = int(salary)
    premium = int(premium)
    result = production * salary + premium
    print('Зарплата данного работника равна: ', result, 'рублей')


calculation()
