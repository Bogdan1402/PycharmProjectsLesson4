class Dog:
    def __init__(self, name: str, age: int, breed: str):
        """

        :param name: Кличка собаки
        :param age: Возраст собаки
        :return:
        """
        self.name = name
        self.age = age
        self.breed = breed
        print("Собака создана")

    def sit(self):
        """Дать команду "Сидеть!" """
        print(f'{self.name.title()} сел')

    def jump(self):
        """Дать команду"Прыжок!"""
        jump_heights = {
            'Дворняга': 1,
            'Овчарка': 2.5,
            'Мопс': 0.5
        }  # Высота прыжка каждой породы
        if self.breed in jump_heights:
            height=jump_heights[self.breed]
            print(f'{self.name.title()} прыгнул на {height} метра(ов)')
        else:
            print(f'{self.name.title()} сделал прыжок')

    def bark(self):
        """Полаять"""
        print(f'{self.name.title()}: гав-гав!')


my_dog = Dog('Бобик', 2, 'Овчарка')
my_dog.bark()
my_dog.jump()
my_dog.sit()
print(my_dog.age)
my_dog_2=Dog('Джони', 4, 'Мопс')
print(my_dog_2.age)
my_dog_2.sit()
my_dog_2.jump()
print(my_dog_2.breed)