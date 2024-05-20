print("Welcome to the Travel Time Calculator")
choice = "y"
while choice == "y":
    miles = float(input("Enter miles: "))
    miles_per_hour = float(input("Enter miles per hour"))

    hour_minutes = round(miles / miles_per_hour)
    minutes_float = round(miles % miles_per_hour)

    print("\nEstimated travel time")
    print("\n-------------------------")
    print(f"Hours {hour_minutes} minutes : {minutes_float}")
    choice = input("Continue? (y/n)")

    # multiply minutes * 60