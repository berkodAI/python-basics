def main():
    expression = input("Expression: " )
    calculate(expression)


def calculate(e):
    x, y , z = e.split(" ")
    if y == '+':
        print(float(x) + float(z))
    elif y == '-':
        print(float(x) - float(z))
    elif y == '*':
        print(float(x) * float(z))
    elif y == '/':
        print(float(x) / float(z))
    else:
        print("Wrong format of expression! Try again")

main()