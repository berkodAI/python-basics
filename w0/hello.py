# A.promt the user for their name
name = input('What is your name?:' )   # variable: container -> name
# '=' sign assign from right to left
# name = input('What is your name?:' ).strip().title()  # another short way

# say hello to user with the name is typed
# print('hello,', name)
# print('hello, ' + name)  # another way to print

# remove whitespace from str
name = name.strip()  # method: strip()

# capitalize user's input:name first letter
# name = name.capitalize()

# capitalize user's input:name first letter of each word
name = name.title()
type(name)

"""
That is a multi-line comment
Here will not be executed
"""

# ----------

# B.parameter - arguments

# inside of print fucntion:
# print(*objects, sep=' ', end='\n', file=sys.str.stdout, flush=False)
# if we do not want to pass to new line we need to overwrite all the parameters inside of the function
# print('hello, ', end='')
# print('hello,', name, sep='???') : sep, end -> named parameters

# escape char:
print('hello, "friend"')
# print("hello, \"friend\"")

#another way of printing variable:
print(f"hello, {name}")  # f string: formatting


# terminal: python
# >>> : interactive mode