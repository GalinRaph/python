import locale
def_coding = locale.getpreferredencoding()
f_n = open("test_file.txt", "w")
f_n.write("сетевое программирование \nсокет \nдекоратор")
f_n.close()
print(f_n)

file_coding = locale.getpreferredencoding()

with open('test_file.txt', encoding=file_coding) as f_n:
    for el_str in f_n:
        print(el_str, end='')
