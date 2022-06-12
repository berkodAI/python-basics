def main():
    felipe("Item: ")


def felipe(prompt):
    tacos = {
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

    total = 0
    while True:  #
        try:
            item = input(prompt).title()  # titlecased
            if item in tacos:
                total += tacos[item]
                print(f"Total: ${total:.2f}")
        except EOFError:
            print() #print(end="\n")
            break
        except KeyError:
            pass


main()
