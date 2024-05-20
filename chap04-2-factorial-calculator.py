print("Welcome to the Factorial Calculator")

choice = "y"
while choice =="y":
    number = int(input("Enter an integer that's greater than 0 and less than 10:"))

    factorial = 1
    for f in range(1, number+1):
        factorial = factorial * f

    print(f"The factorial of {number} is {factorial}")
    choice = input("Continue ? (y/n): ")