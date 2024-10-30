class Animal:
    def __init__(self, name, num_legs):
        self.name = name
        self.num_legs = num_legs

    def move(self):
        print("The animal is moving")


class Dog(Animal):
    def sound(self):
        print("Woof!")


my_animal = Animal("Lion", 4)
print(my_animal.name)
my_animal.move()

dog = Dog("Fido", 4)
dog.sound()
