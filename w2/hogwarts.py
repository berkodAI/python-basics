"""
students = ["Hermione", "Harry", "Ron"]  # list

print(students[2])

"""
# ---- 1
"""
students = ["Hermione", "Harry", "Ron"]  # list

for student in students:
    print(student)

"""

# ---- 2
"""
students = ["Hermione", "Harry", "Ron"]  # list

for i in range(len(students)):
    print(i +1 , students[i])
"""


# ---- 3
"""
#students = ["Hermione", "Harry", "Ron", "Draco"]  # list
#houses = ["Gryffindor", "Gryffindor","Gryffindor", "Slytherin"]  # list

# dict:
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
    }

#print(students["Hermione"])
#print(students["Harry"])
#print(students["Ron"])
#print(students["Draco"])

for student in students:
    #print(student)  # keys: "Hermione", "Harry", etc.
    #print(students[student])  #value: "Gryffindor", etc.
    print(student, students[student], sep=", ")  # another way

"""


# ---- 4

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}  # absence of value: None
]

for student in students:
    #print(student)  # prints all the dictionaries
    print(student["name"], student["house"], student["patronus"], sep=", ")  # prints only names from the dictionaries