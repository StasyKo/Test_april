# 7. Реализовать проект «Операции с комплексными числами». Создайте класс
# «Комплексное число». Реализуйте перегрузку методов сложения и умножения
# комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры
# класса (комплексные числа), выполните сложение и умножение созданных
# экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма чисел равна:')
        return f'{self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение чисел равно:')
        return f' {self.a * other.a - (self.b * other.b)} +' \
               f' {self.b * other.a} * i'

    def __str__(self):
        return f'{self.a} + {self.b} * i'


x = ComplexNumber(55, 20)
y = ComplexNumber(-5, 10)
print(x)
print(y)
print(x + y)
print(x * y)
