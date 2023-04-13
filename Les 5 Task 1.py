# 1. Создать программный файл в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода данных будет
# свидетельствовать пустая строка.

my_f = open('text.txt', 'w')
line = input('Введите текст латинскими буквами \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст латинскими буквами \n')
    if not line:
        break

my_f.close()
my_f = open('text.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()

