# a block of code that does a specific operation

x = 60
y = 40


def add():
    if x > y:
        print(f"{x} is greater than {y}")
    elif x < y:
        print(f"{x} is less than {y}")
    else:
        print(f"{x} is equal to {y}")
    print(f"The sum of {x} and {y} is {x + y}")


def greetPerson():
    name = input("What is your name? ")
    print(f"Hello {name}")


greetPerson()
