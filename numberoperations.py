# A python program that checks whether a number is positive, negative or zero

# number = 5

# if number > 0:
#     print("The number is positive")
# elif number < 0:
#     print("The number is negative")
# else:
#     print("The number is zero")

# A python program that checks whether a number is odd or even

# number2 = int(input("Enter a number: "))
# number3 = int(input("Enter another number: "))

# if number2 % 2 == 0:
#     print(f"{number2} is an even number.")
# else:
#     print(f"{number2} is an odd number.")

# A python program that calculates the square of a number

# number4 = int(input("Enter a number: "))
# square = number4 * number4
# or
# square = number4 ** 2

# print(f"The square of {number4} is {square}")

# Grading System (A, B, C, D, E)
# 0-39 D
# 40-59 C
# 60-79 B
# 80-100 A

maths = int(input("Enter your maths score (0-100): "))
english = int(input("Enter your english score (0-100): "))
physics = int(input("Enter your physics score (0-100): "))
kiswahili = int(input("Enter your kiswahili score (0-100): "))

if maths < 0 or english < 0 or physics < 0 or kiswahili < 0:
    print("Negative scores are not allowed")
elif maths > 100 or english > 100 or physics > 100 or kiswahili > 100:
    print("Scores over 100 are not allowed")
else:  # if all scores are between 0 and 100
    total = maths + english + +physics + kiswahili
    average = round(total / 4, 2)

    if average >= 80:
        print(f"Your average score is {average}. Congratulations! You got an A")
    elif average >= 60 and average < 80:
        print(f"Your average score is {average}. Good job! You got a B")
    elif average >= 40 and average < 60:
        print(f"Your average score is {average}. Good effort! You got a C")
    elif average >= 20 and average < 40:
        print(f"Your average score is {average}. Pull up your grades! You got a D")
    else:
        print(f"Your average score is {average}. You need to work harder! You got an E")
