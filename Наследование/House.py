import time


class House:
    """Дом"""
    def __init__(self, area: float, rooms: int, address: str):
        """

        :param area: Площадь дома
        :param rooms: Количество комнат
        :param address: Адрес
        """
        self.area=area
        self.rooms=rooms
        self.address=address
        self.door_closed=True

    def open_door(self):
        self.door_closed=False
        print(f'Дверь дома по адресу {self.address} открыта')

    def close_door(self):
        self.door_closed = True
        print(f'Дверь дома по адресу {self.address} закрыта')

    def get_door_status(self):
        if self.door_closed:
            return 'Дверь закрыта'
        else:
            return "Дверь открыта"


class MultiStoryHouse(House):
    """Многоэтажный дом"""
    def __init__(self, area: float, rooms: int, address: str, floors: int):
        super().__init__(area, rooms, address) # Вызываем метод родительского класса
        self.floors=floors
        self.elevator_floor = 1 # Этаж на котором стоит лифт
        self.elevator_door_closed = True #Закрыта ли дверь лифта

    def get_floors(self):
        """Возвращает количество этажей."""
        return self.floors

    def call_elevator(self, floor: int):
        """Вызвать лифт
        :param floor: Этаж, куда вызвается лифт.
        """
        floor_time = 3 # Время прохожденния лифта одного этажа (с)
        way = abs(floor - self.elevator_floor)
        total_time = floor_time * way   #Находим время прохождения всех этажей
        print(f'Лифт отправляется с этажа {self.elevator_floor} на этаж {floor}...')
        time.sleep(total_time)
        print('Лифт приехал')
        self.elevator_floor = floor
        self.elevator_door_closed = False
        print('Дверь открыта')
        time.sleep(10)
        self.elevator_door_closed = True
        print('Дверь закрыта')




my_house=House(50,2, 'г. Краснодар, ул. Ленина 6')
print(f'Количество комнаты: {my_house.rooms}')
print(my_house.get_door_status())
my_house.open_door()
print(my_house.get_door_status())
my_house.close_door()

my_house10=MultiStoryHouse(50,2, 'г. Краснодар, ул. Ленина 6', 5)
my_house10.open_door()
my_house10.call_elevator(5)
my_house10.call_elevator(1)
