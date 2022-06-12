def main():
    date()


# output format: YYYY-MM-DD


def date():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    while True:
        date = input("Date: ")  # prompt the user for the date input
        try:
            # split the date input by "/"
            month, day, year = date.split('/')
            # check if month is between 1-12 and day is between 1-31
            if 1 <= int(month) <= 12  and 1<= int(day) <= 31:
                # break out of while loop
                break
        # if the try module scenarios do not occur, we will enter except block and checking other scenarios
        except:
            try:
                # the date in new scenario:
                month2, day2, year = date.split(" ")
                # finding the number(index - position) of the month through each element of the list
                for i in range(len(months)):
                    if month2 == months[i]:
                        month = i + 1  # the index range starts with 0 and ends with 11 so need to add 1 to find the month
                # the day comes with ',' so we need to remove(replace with space) it from
                day = day2.replace(",", "")
                # check if month is between 1-12 and day is between 1-31
                if 1 <= int(month) <= 12  and 1<= int(day) <= 31:
                # break out of while loop
                    break
            except:
                pass  # ask the date again
    # if everything goes well, print the correct format of date as an output
    print(f"{year}-{int(month):02}-{int(day):02}")   # output format: YYYY-MM-DD


main()

