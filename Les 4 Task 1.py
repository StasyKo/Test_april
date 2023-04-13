# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта
# заработной платы сотрудника. Используйте в нём формулу:
# (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для
# конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

if len(argv) > 1:
    name_script, time_work, rate, bonus = argv
    time_work = int(time_work)
    rate = int(rate)
    bonus = int(bonus)
    print((time_work * rate) + prize)
else:
    time_work = int(input('Ведите количество выработанных часов: '))
    rate = int(input('Введите почасовую ставку: '))
    bonus = int(input('Введите размер премии: '))
    print((time_work * rate) + bonus)




