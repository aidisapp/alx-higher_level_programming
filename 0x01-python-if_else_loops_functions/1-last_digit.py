#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

the_last_digit = abs(number) % 10
print(f"Last digit of {number} is {the_last_digit}", end=' ')

if the_last_digit > 5:
    print("and is less than 5")
elif the_last_digit == 0:
    print("and is 0")
else:
    print(f"and is less than 6 and not 0")
