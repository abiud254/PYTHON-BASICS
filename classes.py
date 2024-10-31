# class Animal:
#     def __init__(self, name, num_legs):
#         self.name = name
#         self.num_legs = num_legs
#
#     def move(self):
#         print("The animal is moving")
#
#
# class Dog(Animal):
#     def sound(self):
#         print("Woof!")
#
#
# my_animal = Animal("Lion", 4)
# print(my_animal.name)
# my_animal.move()
#
# dog = Dog("Fido", 4)
# dog.sound()

# class Computer:
#     # attributes
#     name = "Dell"
#
#     # special functions
#     def __init__(self, ram, cpu):
#         self.ram = ram
#         self.cpu = cpu
#
#     # methods
#     def info(self, brand):
#         print(f"This {brand} ---- {self.ram} ---- {self.cpu}")
#
#     # class method
#     @classmethod
#     def compare(cls):
#         print(cls.name)
#
#     # static method
#     @staticmethod
#     def details():
#         print("This is a computer with 8 GB RAM and i7 CPU")
#
#
# # instanciating
# comp1 = Computer("8 GB", "i7")
# comp2 = Computer("8 GB", "i3")
#
# comp1.info("Latitude")
# # comp2.info()
#
# comp1.compare()
# comp1.details()


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # instance method
    def info(self):
        print(f"{self.model} belongs to {self.brand}")


car1 = Car("Toyota", "Sentry", "2015")
car2 = Car("Nissan", "X-Trail", "2014")
car1.info()
