class Car:
    """Машина"""
    # Статический атрибуты
    count = 0
    max_speed = 120

    def __init__(self, color: str):
        self.color=color
        Car.count += 1


    @classmethod
    def get_count(cls):
        """Возвращает количество созданных обЪектов класса"""
        return cls.count





car1 = Car('Green')
car2 = Car('Blue')
car3 = Car('Yellow')

print('Скорость car1:', car1.max_speed)
print('Скорость Car:', Car.max_speed)
print(car3.color)
print('Количество машин:', Car.get_count())
print(car3.get_count())
