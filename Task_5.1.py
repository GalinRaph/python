my_f = open('task_5.1.txt', 'w')
line = input('Введите текст')
while line:
    my_f.writelines(line + '\n')
    line = input('Введите текст')
    if not line:
        break

my_f.close()
