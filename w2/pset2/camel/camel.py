def main():
    name = input("camelCase: ")
    snake_case(name)


def snake_case(n):
    for c in n:
        if c.isupper():  # checking if there is uppercase letter
            c = c.lower()  # lower them
            print("_", end="")  # print "_" before upper case that is founded in string
        print(c, end="")  # prints each letter in string and give a blank space at the end

    print()  # new line at the end


main()