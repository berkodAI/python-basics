
"""
x = int(input("What is x? "))

if x % 2 == 0:
    print("EVEN")
else:
    print("ODD")
"""

# -------------2
"""
def main():
     x = int(input("What is x? "))
     parity(x)


def parity(number):
    if number % 2 == 0:
        print("EVEN")
    else:
        print("ODD")


main()
"""


# ------------3
def main():
     x = int(input("What is x? "))
     if is_even(x):
         print("EVEN")
     else:
         print("ODD")


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    # return True if n % 2 == 0 else False  # same
    # or
    # return n % 2 == 0  # same



main()

