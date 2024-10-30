try:
    no_of_subjects = int(input("Enter the number of subjects: "))
except ValueError:
    print("The number of subjects must be an integer")
    exit()

subjects = {}
total = 0

for i in range(1, no_of_subjects + 1):
    subject = input(f"Enter the name of subject {i}: ")
    while True:
        try:
            marks = int(input(f"Enter the marks for {subject}: "))
            if 0 <= marks <= 100:
                break
            else:
                print("Marks must be between 0 and 100")
                print("Enter the marks for the subject again: ")
        except ValueError:
            print("Marks must be an integer")
    subjects[subject] = marks
    total += marks


average = total / no_of_subjects
grade = "E"
if average >= 80:
    grade = "A"
    print(f"Your average score is {average}. Congratulations! You got an {grade}")
elif average >= 60 and average < 80:
    grade = "B"
    print(f"Your average score is {average}. Good job! You got a {grade}")
elif average >= 40 and average < 60:
    grade = "C"
    print(f"Your average score is {average}. Good effort! You got a {grade}")
elif average >= 20 and average < 40:
    grade = "D"
    print(f"Your average score is {average}. Work harder! You got a {grade}")
else:
    grade = "E"
    print(f"Your average score is {average}. See me! You got an {grade}")

subjects["Total"] = total
subjects["Average"] = int(average)
subjects["Grade"] = grade

print(subjects)
