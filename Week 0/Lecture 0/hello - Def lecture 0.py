def main():
    name = input("What's your name? ")
    hello(name)

# this function can be here or at the top (which does not make much sense) or in another file entirely
def hello(to="world"):
    print("Hello,", to)

main()