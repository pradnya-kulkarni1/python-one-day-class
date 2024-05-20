print("Tip Calculator")

choice = "y"
while choice =="y":

    cost_of_meal = float(input("Cost of meal:  "))
    print("\n15%")
    fifteen_tip = cost_of_meal*0.15
    print(f"Tip amount: ${fifteen_tip:,.2f}")
    print(f"Total amount: ${cost_of_meal+fifteen_tip:,.2f}")
    print()

    print("20%")
    twenty_tip = cost_of_meal*0.2
    print(f"Tip amount: ${twenty_tip:,.2f}")
    print(f"Total amount: ${cost_of_meal+twenty_tip:,.2f}")
    print()
    print("25%")
    twntyf_tip = cost_of_meal*0.25
    print(f"Tip amount: ${twntyf_tip:,.2f}")
    print(f"Total amount: ${cost_of_meal+twntyf_tip:,.2f}")


    choice = input("Continue? (y/n)")