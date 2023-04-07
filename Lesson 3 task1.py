# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def div(a, b):
    try:
        a, b = int(a), int(b)
        my_div = a / b
    except ValueError:
        return 'Ошибка!'
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'
    return round(my_div, 2)

print(div(float(input('Ведите делимое: ')),
          float(input('Введите делитель: '))))



    
