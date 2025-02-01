expression = input("Give an arithmetic expression.\n").split(" ")
void = "Enter a valid format. Ex: x + y"

if len(expression) != 3:
    print(void)
    exit()

op1 = int(expression[0])
symbol = (expression[1])
op2 = int(expression[2])


if symbol == "+":
    result = op1 + op2
elif symbol  == "-":
    result = op1 - op2
elif symbol == "*":
    result = op1 * op2
elif symbol == "/":
    result = op1 / op2
else:
    result = void

result = float(result)
result = round(result, 1)
print(result)
