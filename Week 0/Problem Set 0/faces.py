def main():
    words = convert()
    words = words.replace(":)", "🙂").replace(":(", "🙁")
    print(words)

def convert():
    greet = input("How are you? \n")
    return greet

main()
