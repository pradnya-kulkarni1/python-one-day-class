print("Welcome to functions and exceptions")

#define a function that adds 2 numbers

# def add_function(num1, num2):
#     return num1+num2

# print(f"add_function(5,7)= {add_function(5,7)}")

def add_function(num1, num2=2):
    return num1+num2

print(f"add_function(5) = {add_function(5)}")

# * says that variable is a list
#variable arguments

def add_function(*nbrs):
    sum = 0
    for n in nbrs:
        sum +=n
    return sum

print(f"add_function(2,4,6) = {add_function(2, 4, 6)}")

print(f"add_function(1, 3, 5, 7, 9)= {add_function(1, 3, 5, 7, 9)}")

# line item (product price, product quantity, handling fee(per line item))
def calc_total_function(price, quantity, handling_fee):
    return (price*quantity)+handling_fee

print(f"calc_total_function(20,2,3) = {calc_total_function(20,2,3)}")

print(f"handling_fee = 5, quantity=7, price=10{calc_total_function(handling_fee = 5, quantity=7, price=10)}")

print("\n***********************Exceptions ************************")
def get_whole_number(prompt):
    while True:
        try:
            whole_number = int(input(prompt))
            break
        except ValueError:
            print("Invalid entry, Please try again.")

whole_nbr = get_whole_number("Enter a whole number:")



print("Bye")