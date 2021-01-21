class Car:
    def __init__(self, speed, color, name, direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        self.direction = direction

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self):
        print(f'Машина {self.name} повернула на{self.direction}')

    def show_speed(self):
        pass


class TownCar(Car):
    def __init__(self, speed, color, name, direction):
        super().__init__(speed, color, name, direction)

    def show_speed(self):
        print(f'Её скорость равна', self.speed)
        if self.speed > 60:
            print('Превышение скорости')


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, speed, color, name, direction):
        super().__init__(speed, color, name, direction)

    def show_speed(self):
        print(f'Её скорость равна', self.speed)
        if self.speed > 40:
            print('Превышение скорости')


class PoliceCar(Car):
    pass


towncar = TownCar(60, 'зелёная', 'Солярис', 'право')
towncar.turn()
towncar.show_speed()
towncar.go()
towncar.stop()
workcar = WorkCar(55, 'чёрная', 'Королла', 'лево')
workcar.go()
workcar.show_speed()
workcar.stop()
workcar.turn()
