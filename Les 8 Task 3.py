# 3. Создайте собственный класс-исключение, который должен проверять
# содержимое списка на наличие только чисел. Проверить работу исключения на
# реальном примере. Запрашивать у пользователя данные и заполнять список
# необходимо только числами. Класс-исключение должен контролировать типы
# данных элементов списка.


class Error:
    def __init__(self, *args):
        self.my_list = []
    def my_input(self):
        while True:
            try:
                val = int(input('Введите число и нажмите "Enter": '))
                self.my_list.append(val)
                print(f'Список значений: - {self.my_list} \n ')
            except:
                print(f"Ошибка ввода, вводите только числа")
                try_again = input(f'Попробуйте снова? y/n ')
                if try_again == 'Y' or try_again == 'y':
                    print(try_except.my_input())
                elif try_again == 'N' or try_again == 'n':
                    return f'Программа завершена'
                else:
                    return f'Программа завершена'

try_except = Error(1)
print(try_except.my_input())