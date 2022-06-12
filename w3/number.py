"""
x = int(input("What's x? "))

print(f"x is {x}")    # if we type not int: ValueError: invalid literal
""" # 1

"""
# ValueError:
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer!")

"""


"""
# 2
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer!")
print(f"x is {x}")  # NameError

"""


"""
# 3
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer!")
else:
    print(f"x is {x}")  # NameError
"""


"""

# 4
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer!")
    else:
        break
print(f"x is {x}")

"""

"""

# 5

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:  # statement
            return int(input("What's x? "))
        except ValueError:
            pass #print("x is not an integer!")
        #else:
            #return x  # break from the loop and return the x at the same time

"""

# 6

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:  # statement
            return int(input(prompt))
        except ValueError:
            pass #print("x is not an integer!")
        #else:
            #return x  # break from the loop and return the x at the same time


main()
