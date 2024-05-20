print("Welcome to control structures")

print(f"Use a match command for a CRUD app")
# command = input("Enter a command (list, add , edit): ")
# match command:
#     case "list" :
#         print("List selected")
#     case "add" :
#         print("Add selected")
#     case "edit" :
#         print("Edit selected")
#     case _: #default case 
#         print("Unknown command")

print(f"\n--------------loops--------------")

even_nbrs = [2,4,6,8, 10]

for nbr in even_nbrs:
    print(f"nbr = {nbr}", end = " ")
print()
# range
for i in range(len(even_nbrs)):
    print(f"{i}: {even_nbrs[i]}")

print()
# enumerate
for i in enumerate(even_nbrs):
    print(i, i[0], i[1])

for idx, value in enumerate(even_nbrs):
    print(f"idx = {idx}, value = {value}")
print("---------")
# range including start (inclusive) and 'stop' (exclusive)

for n in range(1,10):
    print(f"n = {n}")
# range including 'step'
print("----------------")
for n in range (0, 10, 2):
    print(f"n = {n}")


print("Bye")