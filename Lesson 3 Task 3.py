# 3. Реализовать функцию my_func(), которая принимает три позиционных
# аргумента и возвращает сумму наибольших двух аргументов.

def my_function(x, y, z):
    my_list = [x, y, z]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return 'Внимание! Вводить только числа!'

print(my_function("dsd", 5698, 2654))
print(my_function(254, 3265, 5465))
print(my_function(float(input('Введите первое число: ')),
                  float(input('Ведите второе число: ')),
                  float(input('Введите третье число: '))))




