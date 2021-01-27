from random import sample
import sys
import os


class LotoCard:
    def __init__(self, player):
        self.name_player = player
        self.value = sample(range(1, 90), 27)
        """Здесь я генерю список, в котором пока нет пропусков,
        sample хорошо использовать для генерирования неповторяющихся чисел"""
        self.place1 = sample(range(0, 9), 4)
        self.place2 = sample(range(0, 9), 4)
        self.place3 = sample(range(0, 9), 4)
        """Здесь я случайно выбираю места в строках карточки,
         в которых ячейки будут пустыми"""
        self.value1 = self.value[0:9]
        self.value1.sort()
        for i in self.place1:
            self.value1[i] = '  '
        self.value2 = self.value[9:18]
        self.value2.sort()
        for i in self.place2:
            self.value2[i] = '  '
        self.value3 = self.value[18:27]
        self.value3.sort()
        for i in self.place3:
            self.value3[i] = '  '
        """Здесь я разбил на три строки, сортирую,
         а затем делаю пропуски в каждой карточке отдельно,чтобы было легче работать,
        я просто не успел придумать и реализовать другой метод"""
        self.array = [self.value1, self.value2, self.value3]
        """Создаю список списков, его и возвращаю. Это и будет нашей карточкой"""


class LotoGame:
    def __init__(self):
        self.barrel = sample(range(1, 91), 90)
        """Я решил сразу сгенерить список очередности бочонков. 
        Честных лотерей не существует"""
        self.keg_number = 0
        """Номер первого бочонка"""
        self.h_counter = 0
        self.c_counter = 0
        """Счётчики для зачёркнутых значений. Я не стал проверять списки
        карточек на наличие незачёркнутых цифр"""

    def start(self, h_player, c_player):
        while True:
            print(f'Карточка {human_player.name_player}а')
            print('__________________________')
            for x in h_player:
                print(' '.join(map(str, x)))
            print('__________________________')
            print(f'Карточка {computer_player.name_player}а')
            print('__________________________')
            for x in c_player:
                print(' '.join(map(str, x)))
            print('__________________________')
            print(f'Готовы сыграть? - Y, нет - N')
            game_word = input(f'---> ')
            if game_word == 'Y' or game_word == 'y':
                while True:
                    print(f' Выпал бочонок: {self.barrel[self.keg_number]}')
                    k_numb = int(self.barrel[self.keg_number])
                    """В дальнейшем значение бочонка будет использоваться для поиска, 
                        в списках, поэтому сразу присваиваю его короткой переменной"""
                    print(f'Карточка {human_player.name_player}а')
                    print('__________________________')
                    for x in h_player:
                        print(' '.join(map(str, x)))
                    print('__________________________')
                    print(f'Карточка {computer_player.name_player}а')
                    print('__________________________')
                    for x in c_player:
                        print(' '.join(map(str, x)))
                    print('__________________________')

                    attempt = input(f'Зачёркиваем карточку? ')
                    if attempt == 'y' or attempt == 'Y':
                        self.h_counter = self.h_counter + 1
                        """Если игрок считает, что номер бочонка в карте есть
                        однозначно повышаем счётчик. Даже если ошибётся, 
                        игра его выкинет"""
                        try:
                            h_player[0].index(k_numb)
                        except ValueError:
                            try:
                                h_player[1].index(k_numb)
                            except ValueError:
                                try:
                                    h_player[2].index(k_numb)
                                except ValueError:
                                    print('Вы ошиблись. Этого значения не было!')
                                    sys.exit()
                        """Я проверяю наличие номера бочонка построчно, поэтому
                        испольузую трёхэтажную конструкцию try. 
                        Потом sys.exit перестала работать, я не разобрался почему, 
                        поэтому заменил её на os.abort"""
                        try:
                            i_elem = h_player[0].index(k_numb)
                            h_player[0].remove(k_numb)
                            h_player[0].insert(i_elem, '--')
                        except ValueError:
                            pass
                        try:
                            i_elem = h_player[1].index(k_numb)
                            h_player[1].remove(k_numb)
                            h_player[1].insert(i_elem, '--')
                        except ValueError:
                            pass
                        try:
                            i_elem = h_player[2].index(k_numb)
                            h_player[2].remove(k_numb)
                            h_player[2].insert(i_elem, '--')
                        except ValueError:
                            pass
                        """Здесь непосредственно замена номера бочонка на -- 
                        в карточке"""
                    else:
                        try:
                            h_player[0].index(k_numb)
                            print('Вы ошиблись номер был в первой строке')
                            os.abort()
                        except ValueError:
                            try:
                                h_player[1].index(k_numb)
                                print('Вы ошиблись номер был во второй строке')
                                os.abort()
                            except ValueError:
                                try:
                                    h_player[2].index(k_numb)
                                    print('Вы ошиблись номер был в третьей строке')
                                    os.abort()
                                except ValueError:
                                    pass
                                """Здесь проверка отсутствия номера бочонка"""
                    try:
                        i_elem = c_player[0].index(k_numb)
                        c_player[0].remove(k_numb)
                        c_player[0].insert(i_elem, '--')
                        self.c_counter = self.c_counter + 1
                    except ValueError:
                        pass
                    try:
                        i_elem = c_player[1].index(k_numb)
                        c_player[1].remove(k_numb)
                        c_player[1].insert(i_elem, '--')
                        self.c_counter = self.c_counter + 1
                    except ValueError:
                        pass
                    try:
                        i_elem = c_player[2].index(k_numb)
                        c_player[2].remove(k_numb)
                        c_player[2].insert(i_elem, '--')
                        self.c_counter = self.c_counter + 1
                    except ValueError:
                        pass
                    """То же самое для ПК"""
                    if self.c_counter == 15:
                        print(f'Победил {computer_player.name_player}')
                        sys.exit(0)
                    else:
                        pass
                    if self.h_counter == 15:
                        """Я проверял при значении в 2 совпадения с бочонком.
                        Программа работает.
                        Вы тоже можете поставить 2, чтобы увидеть, как программа
                        сработает при победе"""
                        print(f'Победил {human_player.name_player}')
                        sys.exit(0)
                    else:
                        pass
                    self.keg_number = self.keg_number + 1
                    """в этот момент мы достём следующий бочонок из мешка"""
            else:
                print('Жаль, что вы не стали играть :(')
                break


human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')
game = LotoGame()
game.start(human_player.array, computer_player.array)

""" Надеюсь использование human_player.array и computer_player.array 
    это не какое-то злостное читерство или нарушение.
    Я не успел поправить карточки так, 
    чтобы все числа находились ровно друг над другом"""
