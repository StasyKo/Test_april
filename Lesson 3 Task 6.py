# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских
# букв и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

def int_func():
    for word in input('Введите слово маленькими латинскими буквами: ').split():
        chars = 0
        for char in word:
            if 97 <= ord(char) >= 122: # диапазон для маленьких лат. букв
                char += 1
        print(word.title())

int_func()


