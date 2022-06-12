def main():
    greetings = input("Greeting: ")
    check(greetings)


def check(g):
    g = g.lower().strip()
    if g.startswith("hello"):
        print("$0")
    elif g.startswith('h'):
        print("$20")
    else:
        print("$100")


main()