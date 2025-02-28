print("Welcome to Lists and Dictionaries!")
# A string: chars stored in order
bob_marley_name = "Robert Nesta Marley"

# A list: ordered and changeable, denoted by square brackets
songs = ["Jamming", "Three Little Birds", "No Woman No Cry"]

# A tuple: ordered and NOT changeable, denoted by parenthesis
# Note: this tuple is not complete. Bob Marley had a lot of kids!
children = ("Sharon", "David 'Ziggy'", "Stephen", "Robert 'Robbie'", "Julian", "Ky-Mani", "Damian")

#processing a string - bob_marley_name
bob_marley_name = "Robert Nesta Marley"
print('bob_marley_name:', bob_marley_name)
print('length of bob_marley_name', len(bob_marley_name))

#get first name of bob_marley_name
# where's the first space?
idx_1 = bob_marley_name.index(" ")
f_bob_marley_name = bob_marley_name[0:idx_1]
print(f"First name: {f_bob_marley_name}")

f_bob_marley_name = bob_marley_name[0:idx_1]
print('first char:', f_bob_marley_name[0:idx_1])

idx_2 = bob_marley_name.index(" ", idx_1+1)
m_bob_marley_name = bob_marley_name[idx_1+1: idx_2]
print(f"Middle name: {m_bob_marley_name}")
l_bob_marley_name = bob_marley_name[idx_2+1:len(bob_marley_name)]
print(f"Last name: {l_bob_marley_name}")

for str in bob_marley_name:
    print(str, end=" ")


print("\n------------------------process songs in a list -----------------")
# process the songs in a list
# use square brackets and slicing
#songs = ["Jamming", "Three Little Birds", "No Woman No Cry"]
print(f"songs:                      {songs}")
print(f"song 1:                     {songs[0]}")
print(f"last song songs[2]:         {songs[2]}")
print(f"last song songs[-1]:        {songs[-1]}")
print(f"last 2 songs songs[1:3]:    {songs[1:3]}")

#append a song to the end
songs.append('temp song')
print(f"temp song added to end:     {songs}")

#change a song/item
songs[3] = "Bobs so cool - not a real song"
print(f"song 3 changed:             {songs}")

# remove the last song and return it
rem_song = songs.pop()
print(f"removed song:               {rem_song}")
print(f"songs:                      {songs}")

print(list(range(10)))
print(list(range(0,20,2)))
print(list(range(0,-10,-1)))
print(list(range(0,20,3)))

# in keyword - text for existence in a list:
print("'in' keyword - is 2 in the list?")

numbers_list = [1, 2, 1, 3, 1, 4, 1, 5]
if 2 in numbers_list:
    print("yep, 2 is in there!")

print("--------------------dictionaries--------------------")

# dictionaries
# dictionary key/value can contain any data type
# can access by get method or square brackets
print("\ndictionaries")
spanish_english = {
    "uno": "one",
    "dos": "two",
    "tres": "three",
    1: "one"
}
print(spanish_english)
# get value by key
print(spanish_english.get("dos"))
print(spanish_english[1])
# add elements to a dictionary using square brackets (no add function)
spanish_english["quatro"] = "four"
print(spanish_english)

#iterate over dictionary keys using for .. in
print("\nIterate over dictionary w/ for .. in")
for key in spanish_english:
    print(f"{key} means {spanish_english[key]}")

print("Bye!")