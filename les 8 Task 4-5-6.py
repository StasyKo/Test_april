# 4. Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым для
# классов-наследников. Эти классы — конкретные типы оргтехники (принтер,
# сканер, ксерокс). В базовом классе определите параметры, общие для
# приведённых типов. В классах-наследниках реализуйте параметры, уникальные
# для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые
# отвечают за приём оргтехники на склад и передачу в определённое подразделение
# компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру
# (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
# вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.

class Store:

    def __init__(self, name, price, quantity, num_in_list, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = num_in_list
        self.my_store_all = []
        self.my_store = []
        self.my_unit = {'Модель': self.name,
                        'Цена за единицу': self.price,
                        'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'
    def reception(self):
        try:
            unit = input(f'Введите наименование модели устройства ')
            unit_p = int(input(f'Введите цену за единицу продукции '))
            unit_q = int(input(f'Введите количество штук '))
            unique = {'Модель устройства': unit, 'Цена за единицу': unit_p,
                      'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Новый товар -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Завершение ввода данных - 0, продолжение работы - Enter')
        q = input(f'---> ')
        if q == '0':
            self.my_store_all.append(self.my_store)
            print(f'Складской список -\n {self.my_store_all}')
            return f'Конец сессии'
        else:
            return Store.reception(self)
class Printer(Store):
    def to_print(self):
        return f'to print s {self.numb} times'
class Scanner(Store):
    def to_scan(self):
        return f'to scan s {self.numb} times'
class Copier(Store):
    def to_copier(self):
        return f'to copier s  {self.numb} times'


unit_1 = Printer('Sony', 8526, 6, 52)
unit_2 = Scanner('HP', 1200, 5, 10)
unit_3 = Copier('DPN', 15, 1, 13)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())