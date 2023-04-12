# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления
# на ноль. Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class Div_By_Null:
    def __init__(self, div, denom):
        self.div = div
        self.denom = denom

    @staticmethod
    def divide_by_null(div, denom):
        try:
            return (div / denom)
        except:
            return (f'На ноль делить нельзя!')

div = Div_By_Null(10, 100)

print(Div_By_Null.divide_by_null(0, 10))
print(Div_By_Null.divide_by_null(20, 5))
print(div.divide_by_null(258, 0))
print(Div_By_Null.divide_by_null(658.2, 0))
print(Div_By_Null.divide_by_null(78569, 0.1))
print(div.divide_by_null(1365, 0.65))