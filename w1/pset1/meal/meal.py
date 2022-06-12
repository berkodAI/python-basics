def main():
    time = input("What time is it? ")
    convert(time)


def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes) / 60  # minutes in 1 hour (float)
    hours = float(hours)  # hours (float)

    time = hours + minutes

    

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        print("Not meal time")


if __name__ == "__main__":
    main()