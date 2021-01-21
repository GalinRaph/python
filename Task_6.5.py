class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки', self.title)


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} Запуск отрисовки ручкой')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}. Запуск отрисовки карандашом')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}. Запуск отрисовки маркером')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
pen.draw()
pencil.draw()
handle.draw()
