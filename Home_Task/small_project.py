# Проект демонстрирует основные функции ООП, такие, как: наследование, инкапсуляция, полиморфизм

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def say_hello(self):
        print("Hello, my name is", self.name)

    def is_drive(self):
        print("I can drive a car" if self.get_age() >= 18 else "I can't drive a car")

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def say_hello(self):
        print("Hi, I'm", self.name, "and I'm studying", self.major)


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def say_hello(self):
        print("Good day, I'm", self.name, "and I teach", self.subject)


if __name__ == '__main__':
    person1 = Person("Ivan", 15)
    person2 = Student("Vasiliy", 20, "Computer Science")
    person3 = Teacher("Petr", 30, "Mathematics")

    person1.say_hello()  # >> Hello, my name is Ivan 
    person1.is_drive()  # >> I can't drive a car
    person2.say_hello()  # >> Hi, I'm Vasiliy and I'm studying Computer Science
    person2.is_drive()  # >> I can drive a car
    person3.say_hello()  # >> Good day, I'm Petr and I teach Mathematics
