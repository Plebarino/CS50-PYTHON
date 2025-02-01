# ask user for input
name = input("Whats your name? ").strip().title()

# splits user's name in to first name and last name
# split returns a sequence of values
first, last = name.split(" ")

# remove whitespace from string
# name = name.strip()

# capitalize first letter of each word
## name = name.capitalize()
## name = name.title()

# you can combine the above two functions BUT if you look @ line 2 you can combine all of it within the input
## name = name.strip().title()


# say hello to user
## OR - print("Hello,", name + ".")
## OR - print("Hello,", name + ".")

# doing it this way removes the parameter of the new line \n
## OR
##print("Hello, ", end="")
##print(name + ".")

# this uses an f string
# if the user passes in their full name it will only return the first, because of .split() which was called earlier.
print(f"Hello, {first}")

