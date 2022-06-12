def main():
    message = input("What do you wanna say?: ")
    playback(message)


def playback(m):
    print(m.replace(" ", "..."))


main()