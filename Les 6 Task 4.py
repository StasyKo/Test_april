# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начала движение'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость для городской машины {self.name} -'
              f' {self.speed}')

        if self.speed > 40:
            return f'{self.name} Превысила допустимую для городских машин' \
                   f' скорость'
        else:
            return f'У {self.name} нормальная скорость'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочей {self.name} - {self.speed}')

        if self.speed > 60:
            return f'{self.name} превысила допустимую для рабочих машин ' \
                   f'скорость '


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из управления полиции.'
        else:
            return f'{self.name} не полицейская машина.'


audi = SportCar(65, 'Красная', 'Ауди', False)
mazda = TownCar(45, 'Белая', 'Мазда', False)
mersedes = WorkCar(75, 'Серый', 'Мерседес', True)
infinity = PoliceCar(120, 'Серебро', 'Инфинити', True)
print(mersedes.turn_left())
print(f'Когда {mazda.turn_right()}, тогда {audi.stop()}')
print(f'{mersedes.go()} с нормальной скоростью, '
      f'но потом {mersedes.show_speed()}')
print(f'{mersedes.name} - {mersedes.color}')
print(f'{audi.name} полицейская машина? {audi.is_police}')
print(f'{mersedes.name}  полицейская машина? {mersedes.is_police}')
print(audi.show_speed())
print(mazda.show_speed())
print(infinity.police())
print(infinity.show_speed())
