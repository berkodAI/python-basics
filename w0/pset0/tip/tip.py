def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO  # DONE
    # gets the user input and remove '$' sign and convert into a float number
    float_dollar = float(d.removeprefix('$'))
    return float_dollar


def percent_to_float(p):
    # TODO  # DONE
    # gets teh user input and remove '%' sign and convert into a float number and divide by 100
    float_percent = float(p.removesuffix('%')) / 100
    return float_percent


main()