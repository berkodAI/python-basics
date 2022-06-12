## [Pset2](https://github.com/berdii/python-basics/tree/main/w2/pset2) :

* 1) [camelCase](https://github.com/berdii/python-basics/tree/main/w2/pset2/camel)

![imagen](https://user-images.githubusercontent.com/97915480/173244975-857acaa6-147a-4138-bed4-3979f0bfb8f8.png)


In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called name, a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.

Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase. For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.

In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

* 2) [Coke Machine](https://github.com/berdii/python-basics/tree/main/w2/pset2/coke)

![imagen](https://user-images.githubusercontent.com/97915480/173245016-2f6c7f93-a5ab-492e-8e4c-486c082a91fb.png)


Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

* 3) [Just setting up my twttr](https://github.com/berdii/python-basics/tree/main/w2/pset2/twttr)

      just setting up my twttr

        — jack⚡️ (@jack) March 21, 2006
             

When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

* 4) [Vanity Plates](https://github.com/berdii/python-basics/tree/main/w2/pset2/plates)

![imagen](https://user-images.githubusercontent.com/97915480/173245058-a6d2d391-6b9e-4d41-8515-c22eeb33d1b4.png)

In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

* “All vanity plates must start with at least two letters.”
* “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
* “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
* “No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

        def main():
            plate = input("Plate: ")
            if is_valid(plate):
                print("Valid")
            else:
                print("Invalid")


        def is_valid(s):
            ...


        main()
      

* 5) [Nutrition Facts](https://github.com/berdii/python-basics/tree/main/w2/pset2/nutrition)

The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”

In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

