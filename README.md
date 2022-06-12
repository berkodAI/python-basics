# Problem Sets

## [Pset0](https://github.com/berdii/python-basics/tree/main/w0/pset0)  :

* 1) [Indoor Voice](https://github.com/berdii/python-basics/tree/main/w0/pset0/indoor)

WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. 
Punctuation and whitespace should be outputted unchanged. 
You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.

### How to Test

Here’s how to test your code manually. At the indoor/ $ prompt in your terminal: :

* Run your program with python indoor.py. Type HELLO and press Enter. Your program should output hello.
* Run your program with python indoor.py. Type THIS IS CS50 and press Enter. Your program should output this is cs50.
* Run your program with python indoor.py. Type 50 and press Enter. Your program should output 50.


* 2) [Playback Speed](https://github.com/berdii/python-basics/tree/main/w0/pset0/playback)

Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).


* 3) [Making Faces](https://github.com/berdii/python-basics/tree/main/w0/pset0/faces)

Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.



* 4) [Einstein](https://github.com/berdii/python-basics/tree/main/w0/pset0/einstein)

Even if you haven’t studied physics (recently or ever!), you might have heard that , wherein  represents energy (measured in Joules),  represents mass (measured in kilograms), and  represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

* 5) [Tip Calculator](https://github.com/berdii/python-basics/tree/main/w0/pset0/tip)

And now for my Wizard tip calculator.

        — Morty Seinfeld

In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written a tip calculator for you, below!

        def main():
            dollars = dollars_to_float(input("How much was the meal? "))
            percent = percent_to_float(input("What percentage would you like to tip? "))
            tip = dollars * percent
            print(f"Leave ${tip:.2f}")


        def dollars_to_float(d):
            # TODO


        def percent_to_float(p):
            # TODO


        main()

Well, we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:

* dollars_to_float, which should accept a str as input (formatted as $xx.xx, wherein each x is a decimal digit), remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
* percent_to_float, which should accept a str as input (formatted as xx%, wherein each x is a decimal digit), remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.

Assume that the user will input values in the expected formats.

## [Pset1](https://github.com/berdii/python-basics/tree/main/w1/pset1) :

* 1) [Deep Thought](https://github.com/berdii/python-basics/tree/main/w1/pset1/deep)

    “All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
    “You’re really not going to like it,” observed Deep Thought.
    “Tell us!”
    “All right,” said Deep Thought. “The Answer to the Great Question…”
    “Yes…!”
    “Of Life, the Universe and Everything…” said Deep Thought.
    “Yes…!”
    “Is…” said Deep Thought, and paused.
    “Yes…!”
    “Is…”
    “Yes…!!!…?”
    “Forty-two,” said Deep Thought, with infinite majesty and calm.”

    — The Hitchhiker’s Guide to the Galaxy, Douglas Adams
    
    In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
    
    
    
* 2) [Home Federal Savings Bank](https://github.com/berdii/python-basics/tree/main/w1/pset1/bank)


[In season 7, episode 24 of Seinfeld](https://youtu.be/IN6cJ_wGmsk), Kramer visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.

In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

* 3) [File Extensions](https://github.com/berdii/python-basics/tree/main/w1/pset1/extensions)

Even though Windows and macOS sometimes hide them, most files have file extensions, a suffix that starts with a period (.) at the end of their name. For instance, file names for GIFs end with .gif, and file names for JPEGs end with .jpg or .jpeg. When you double-click on a file to open it, your computer uses its file extension to determine which program to launch.

Web browsers, by contrast, rely on media types, formerly known as MIME types, to determine how to display files that live on the web. When you download a file from a web server, that server sends an HTTP header, along with the file itself, indicating the file’s media type. For instance, the media type for a GIF is image/gif, and the media type for a JPEG is image/jpeg. To determine the media type for a file, a web server typically looks at the file’s extension, mapping one to the other.

In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

     * .gif
     * .jpg
     * .jpeg
     * .png
     * .pdf
     * .txt
     * .zip

If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

* 4) [Math Interpreter](https://github.com/berdii/python-basics/tree/main/w1/pset1/interpreter)

Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables. But let’s write a program that enables users to do math, even without knowing Python.

In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

* x is an integer
* y is +, -, *, or /
* z is an integer

For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!

* 5) [Meal Time](https://github.com/berdii/python-basics/tree/main/w1/pset1/meal)

Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?

In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).


      def main():
          ...


      def convert(time):
          ...


      if __name__ == "__main__":
          main()
          

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


## [Pset3](https://github.com/berdii/python-basics/tree/main/w3/pset3) :

* 1) [Fuel Gauge](https://github.com/berdii/python-basics/tree/main/w3/pset3/fuel)

![imagen](https://user-images.githubusercontent.com/97915480/173245149-dc2d3d44-2fd8-4bc1-a209-151951191bb7.png)


Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

* 2) [Felipe’s Taqueria](https://github.com/berdii/python-basics/tree/main/w3/pset3/taqueria)

![imagen](https://user-images.githubusercontent.com/97915480/173245223-0cdcb553-6968-48e4-a1dc-cb4cfe8c64b5.png)

One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, which offers a menu of entrees, per the dict below, wherein the value of each key is a price in dollars:

        {
            "Baja Taco": 4.00,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
        }
        

In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.


* 3) [Grocery List](https://github.com/berdii/python-basics/tree/main/w3/pset3/grocery)

Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

* 4) [Outdated](https://github.com/berdii/python-basics/tree/main/w3/pset3/outdated)

In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:


              [
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
              
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.


