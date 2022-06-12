# --- 1
"""
for _ in range(3):
    print("#")
"""

# ---- 2
"""
def main():
    print_column(3)
    print_row(4)


def print_column(height):
    for _ in range(height):
        print("#")
    # or - >
    # print("#\n" * height, end="") # same as above


def print_row(width):
    print("?" * width)

main()
"""

# --- 3

def main():
    print_square(3)  # 3x3


def print_square(size):  # size: both for height and width
    # for each row in square
    for h in range(size):  # row
        # for each brick in row
        for w in range(size):  # column
            # print brick
            print("#", end="")
        # space
        print()

    # another shorter way:
    # for h in range(size):
        # print("#" * size)  #or # print_row(size)

def print_row(width):
    print("#" * width)

main()