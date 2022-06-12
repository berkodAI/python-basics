def main():
    # prompt the user for input emoji
    mood = input()
    # convert emoticons into a corresponding emoji
    result = convert(mood)
    # print the result
    print(result)


def convert(str):
    # Happy emoji:
    happy = str.replace(":)", "🙂")

    # Sad emoji:
    sad = happy.replace(":(", "🙁")

    # return the str:
    return sad


main()
