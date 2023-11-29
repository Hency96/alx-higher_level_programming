#!/usr/bin/python3
import random
number = random.randint(-10, 10)
n_number = number
if n_number < 0:
    print(f"{n_number} is negative")
elif n_number == 0:
    print(f"{n_number} is zero")
else:
    print(f"{n_number} is positive ")
