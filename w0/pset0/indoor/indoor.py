# main function
def main():
    # prompt the user for the message
    m = input("What do you wanna say?: ")
    # calling the indoor() function to indoor voice (lowercase)
    indoor(m)


# indoor function that gets the message that typed in by user and print in lowercase
def indoor(message):
    low = message.lower()
    print(low)


main()  # calling the main() function to execute indoor.py