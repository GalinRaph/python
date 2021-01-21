class Worker:

    def __init__(self):
        self.name = 'Юстас'
        self.surname = 'Алекс'
        self.position = 'Управляющий над всеми управляющими'
        self._income = {'wage': 55000, 'bonus': 1000}


class Position(Worker):
    def get_full_name(self):
        print(self.position, self.name, self.surname)

    def get_total_income(self):
        print(f' полная зарплата составляет', self._income["wage"] + self._income['bonus'])


position = Position()
position.get_full_name()
position.get_total_income()
