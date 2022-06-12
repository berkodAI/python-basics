def main():
    # prompt the user for the answer
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    # checking the user input
    check(answer)
    # print(answer)


def check(a):
    # case- and space-insensitively.
    a = a.lower().strip()
    # checkin if the answer is "42"
    if a == "42" or a == "forty-two" or a == "forty two":
        print("Yes")
    else:
        print("No")


main()