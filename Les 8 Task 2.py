# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления
# на ноль. Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class DivByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return divider / denominator
        except:
            return f'Делить на ноль нельзя!'


div = DivByNull(58, 10)
print(DivByNull.divide_by_null(2584, 0))
print(DivByNull.divide_by_null(856, 0.6))
print(div.divide_by_null(156, 0))
