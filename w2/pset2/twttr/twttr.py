def main():
    twit = input("Input: ")
    shorten(twit)



def shorten(s):
    for c in s:
        if c.isalpha():
            vowels = "A, E, I, O, U"
            if c.isupper():
                txt = c.strip(vowels)
                print(txt, end="")
            else:
                txt = c.strip(vowels.lower())
                print(txt, end="")
        else:
            print(c, end="")

    print()


main()