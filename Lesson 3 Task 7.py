# 7. Продолжить работу над заданием. В программу должна попадать строка из
# слов, разделённых пробелом. Каждое слово состоит из латинских букв в нижнем
# регистре. Нужно сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def int_func(word):
    lat_char = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(lat_char) else False

words = input('Ввудите строку из слов через пробел: ').split()
for i in words:
    res = int_func(i)
    if res:
        print(res, ' ')

int_func()
