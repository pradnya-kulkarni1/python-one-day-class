print("Welcome to the Temperature Converter")

choice = "y"
while choice == "y":
    degrees_faren = float(input("Enter degrees in farenheit"))
    c = (degrees_faren - 32)* 5/9
    print(f"Degrees in Celcius: {c:,.2f}")
    choice= input("Continue (y/n)?")