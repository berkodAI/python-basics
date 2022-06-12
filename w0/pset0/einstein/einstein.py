def main():
    # prompt the user for the mass (in kilograms)
    mass = int(input("m: "))
    # call the energy() function for calculation using the mass that is provided by user
    energy(mass)


def energy(m):
    # speed of light (meters per second)
    c = 300000000  # 3E8
    # Energy formula (in Joules)
    E = m * (c ** 2)
    print(f"E: {E}")  # print(f"E: {E:,}")


main()