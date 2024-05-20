print("Welcome to the Letter Grade Converter")

choice = "y"
while choice == "y":

    numerical_grade = int(input("Enter Numberical grade"))
    if numerical_grade >87 <100:
        print("Letter Grade: A")
    elif numerical_grade > 80 < 87:
        print("Letter Grade: B")
    elif numerical_grade > 67 < 79:
        print("Letter Grade: C")
    elif numerical_grade > 60 < 67:
        print("Letter Grade: D")
    else:
        print("Letter Grade: F")
    choice = input("Continue? (y/n)")

