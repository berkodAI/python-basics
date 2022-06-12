def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # vanity plates may contain min 2 - max 6 chars (letters or numbers)
    if len(s) < 2 or len(s) > 6:
        return False

    # Vanity plates must start at least with 2 letters
    if s[0:2].isalpha() == False:
        return False

    # numbers can not be used in the middle of the plate. must come at the end.
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    # first number cannot be "0"
    indx = 0
    while indx < len(s): # while there are still letters or numbers left in our plate
        if s[indx].isalpha() == False:
            if s[indx] == "0":
                return False
            else:
                break
        indx += 1  # checking the next char of our plate till the end of our string

    # Periods, spaces or punction marks arenot allowed in the plate
    for c in s:
        marks = {'.', ' ', '!', '?'}
        if c in marks:
            return False

    # if each checking conditions goes well:
    return True


main()