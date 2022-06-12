def main():
    time = input("What time is it? ")
    convert(time)


def convert(time):
    hours, min_timeperiod = time.rsplit(":")
    minutes, time_period = min_timeperiod.split(" ")
    # print(minutes)
    minutes = float(minutes) / 60  # minutes in 1 hour (float)
    hours = float(hours)  # hours (float)

    time = hours + minutes
    if time_period == 'a.m.':
        if 7 <= time <= 8:
            print("breakfast time")
        else:
            print("Not meal time")
    elif time_period == 'p.m.':
        if 0 <= time <= 1:
            print("lunch time")
        elif 6 <= time <= 7:
            print("dinner time")
        else:
            print("Not meal time")


if __name__ == "__main__":
    main()