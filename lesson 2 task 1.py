# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать
# функцию type() для проверки типа. Элементы списка можно не запрашивать у
# пользователя, а указать явно, в программе/

new_int = 8
new_str = "str"
new_list = ['9', 'kl']
new_tuple = ('b', '77')
new_set = {1, 2.3, True, "bdh"}
new_dict = {1: 'Jerry', 2: 'Tom'}
big_list = [new_int, new_str, new_tuple, new_set, new_dict,]
for i in big_list:
    print(f'{i} -  {type(i)}')




