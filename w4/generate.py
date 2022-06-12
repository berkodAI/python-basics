#1
"""
import random

coin = random.choice(["heads", "tails"])
print(coin)
"""


#2
"""
from random import choice

coin = choice(["heads", "tails"])
print(coin)
"""

#3
"""
import random
number = random.randint(1, 10)  # randin(a, b) both inclusive
print(number)
"""
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)