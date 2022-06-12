def main():
    frac = get_fraction("Fraction: ")
    while True:
        if frac <= 100:
            break
        else:
            frac = get_fraction("Fraction: ")

    if 99 <= frac <= 100:
        print("F")
    elif frac <= 1:
        print("E")
    else:
        print(f"{frac}%")


def get_fraction(prompt):
    while True:
        try:
            fraction = input(prompt)  # X/Y - fraction - fuel in the tank
            X, Y = [int(d) for d in fraction.split('/')]
            #X, Y = list(map(int, fraction.split('/')))  # another way of cating to int:  map the function int on each substring
            f = X / Y
            return round(f*100)
        except (ValueError, ZeroDivisionError):
            pass


main()