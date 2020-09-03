# game_randomnumber.py

# import modul random
import random

# initialize random number generator
random.seed()

# random values and calculation
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b

print("the task:", a, "+", b)

#
print("Your solution: ")
# takes your input from the console
z = input()

# Output
print("Ihre Eingabe:", z)
print("Das Ergebnis:", c)
