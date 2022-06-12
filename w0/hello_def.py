
"""
def hello(to="world"):
    print("hello,", to)

# scope : refers to the location where variables value is valid
#         where is available to you to use

hello()
name = input("What is your name?:" )
hello(name)
"""

# -----------

# another way

def main():
    name = input("What is your name?:" )
    hello(name)


def hello(to="world"):
    print("hello,", to)


main()