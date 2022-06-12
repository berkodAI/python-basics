def main():
    shopping()


def shopping():
    item_dict = {}
    while True:
        try:
            item = input().lower()
            if item in item_dict:
                item_dict[item] += 1  # adding 1 to the count if the item exist
            else:
                item_dict[item] = 1  # if not initialize it: 1
        except EOFError:
            for key in sorted(item_dict.keys()):  # getting all the items in the dict and sort them
                print(item_dict[key], key.upper())
            break


main()