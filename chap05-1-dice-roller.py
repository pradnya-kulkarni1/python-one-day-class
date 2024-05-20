import random


print("Dice Roller")
roll = input("Roll the dice? (y/n): ")
while roll == "y":
    die_roll1 = random.randint(1,6)
    die_roll2 = random.randint(1,6)
    print("\n")
