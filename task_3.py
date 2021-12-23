try:
    word_one = b'attribute'
    print(f' word_one возможно записать в байтовом типе')
except SyntaxError:
    print(f'word_one невозможно записать в байтовом типе')
try:
    word_two = b'класс'
    print(f' word_two возможно записать в байтовом типе')
except SyntaxError:
    print(f' word_two невозможно записать в байтовом типе')
try:
    word_tree = b'функция'
    print(f' word_tree возможно записать в байтовом типе')
except SyntaxError:
    print(f' word_tree невозможно записать в байтовом типе')
try:
    word_four = b'type'
    print(f'word_four возможно записать в байтовом типе')
except SyntaxError:
    print(f'word_four невозможно записать в байтовом типе')

