print("Welcome to the Squares and Cubes table")

choice = "y"
while choice == "y":

    number = int(input('Enter an integer'))
    print()

    print(f"number\tSquared\tCubed")
    print("====\t====\t====")

    for n in range(1,number+1):
   
        print(f"{n}\t{n*n}\t{n*n*n}")
    choice = input("Continue? (y/n)")
