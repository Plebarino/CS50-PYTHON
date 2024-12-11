x = float(input("What's x? "))
y = float(input("What's y? "))

## standard method to specify how many digits to print
#z = round(x / y, 2)
#print(z)

z = x / y
# how to specify using an f string how many digits to print
print(f"{z:.2f}")
