"""
i = 0
while i < 3:
    print("meow")
    i += 1
"""

#----1


# for
""" same 1
for i in [0, 1, 2]:
    print("meow")
"""
#----2

""" same 2
for index in range(3):
    print("meow")
"""
#----3

""" same 3
for _ in range(3):
    print("meow")
"""
#----4

# print("meow\n" * 3, end="")  # same 4   # end="" -> deletes a blanck space at the end

#----5
"""
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
"""

#---- 6
def main():
    number = get_number()
    meow(number)


def get_number():
     while True:
        n = int(input("What's n? "))
        if n > 0:
            return n  # also break from the loop


def meow(n):

    for _ in range(n):
        print("meow")


main()

#---- 7



