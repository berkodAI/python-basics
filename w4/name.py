# sys: system
# sys.argv : argument vector : is a list

import sys  # module : library
"""
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
"""


# 2
"""
# check for errors
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
# print name tags
    print("hello, my name is", sys.argv[1])
"""

# 3
"""
if len(sys.argv) < 2:
    sys.exit("Too few arguments")  # will print the string inside and exit
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])
"""


#4
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]: # slice from first element of list till end
    print("hello, my name is", arg)