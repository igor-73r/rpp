class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


if __name__ == '__main__':
    animal = Animal()
    dog = Dog()
    cat = Cat()

    animal.sound()  # >> "Animal makes a sound"
    dog.sound()  # >> "Dog barks"
    cat.sound()  # >> "Cat meows"
