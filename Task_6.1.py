from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = ['красный', 'жёлтый', 'зелёный']

    def running(self):
        i = 0
        print(f' Загорелся {self.__color[i]} цвет')
        sleep(7)
        i += 1
        print(f' Загорелся {self.__color[i]} цвет')
        sleep(2)
        i += 1
        print(f' Загорелся {self.__color[i]} цвет')
        sleep(2)


trafficlights = TrafficLight()
for i in cycle('Цикл'):
    (trafficlights.running())
