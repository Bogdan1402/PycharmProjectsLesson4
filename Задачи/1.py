class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def get_info(self):
        print(f'Имя {self.name}, Возраст {self.age}')


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id=student_id

    def get_info(self):
        print(f'Имя {self.name}, Возраст {self.age}, Номер студенческого билета {self.student_id}')



person1 = Person('Богдан', 12)
person1.get_info()
person2 = Student('Назар', 21, 2391)
person2.get_info()

