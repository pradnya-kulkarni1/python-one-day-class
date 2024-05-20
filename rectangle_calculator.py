print("Welcome to the Area and Perimeter Calculator")

choice = "y"
while choice == "y":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width

    perimeter = 2* length + 2* width 

    print(f"Area: {area}")

    print(f"Perimeter: {perimeter}")
    choice = input("Continue? (y/n)")