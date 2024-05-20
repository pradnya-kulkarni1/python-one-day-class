import random


print("Welcome to the Guess the Number Game")
print("++++++++++++++++++++++++++++++++++++")

choice = "y"
while choice =="y":     
    print("\n I'm thinking of a number from 1 to 100.\n Try to guess it\n")
    guess = random.randint(1,100)

    number = int(input("Enter number: "))

    while number != guess:
        
        if number < guess :
            if number > guess - 10:
                print("Your guess is little low!")
                number = int(input("Enter number"))

            print("Way to low! Guess again")
            number = int(input("Enter number"))
        
        else:
            if number > guess:
                if number < guess - 10:
                    print("Your guess is little low!")
                    number = int(input("Enter number"))
            print("Way to high! Guess again")
            number = int(input("Enter number"))

    
    print("Great work! You are a mathematical wizard.")
    
    choice=input("Continue?(y/n): ")