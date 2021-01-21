class Road:
    def __init__(self, roadlength, roadwidth, roadthickness):
        self._length = roadlength
        self._width = roadwidth
        self._thickness = roadthickness

    def get_calculation(self):
        weight = self._length * self._width * 25 * self._thickness
        print(f'Необходимая масса асфальта =  {weight} кг')


user_length = int(input('Введите длину дороги в метрах: '))
user_width = int(input('Введите ширину дорогив в метрах: '))
user_thickness = int(input('Введите толщину дороги в сантиметрах: '))
user_road = Road(user_length, user_width, user_thickness)
user_road.get_calculation()
