# 4. Программа принимает действительное положительное число x и целое
# отрицательное число y. Выполните возведение числа x в степень y. Задание
# реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись
# без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в
# степень с помощью оператора **. Второй — более сложная реализация без
# оператора **, предусматривающая использование цикла.

def my_func(x, y):
    try:
        x,y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'Ошибка ввода данных!'
        else:
            res = 1
            for _ in range(abs(y)):
                res /= x
            return f'Результат равен {round(res), 2}'
    except ValueError:
        return 'Внимание, вводить только числа!'
num_1 = input('Введите действительное положительное число: ')
num_2 = input('Введите целое отрицательное число: ')

print(my_func(num_1, num_2))



