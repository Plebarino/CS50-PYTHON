greeting = input()
greeting.lower


if greeting[0] == "h" and "hello" in greeting:
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")
