# def greet(age: int, name="Guest"):
# print(f"Hello, {name}! You are {age} years old.")


# def avrg(a: int, b: int, c: int):
# return (a + b + c) / 3


# greet(10)
# print(avrg(10, 20, 30))


def hypotenuse_calculator(side_a=1, side_b=1):
    hypotenuse = (side_a**2 + side_b**2) ** (1 / 2)
    return round(hypotenuse, 2)


print(hypotenuse_calculator(side_a=5, side_b=10))


def numbers(*args):
    return sum(args)


def details(**kwargs):
    print(kwargs)


details(a=1, b=2, c=3)
