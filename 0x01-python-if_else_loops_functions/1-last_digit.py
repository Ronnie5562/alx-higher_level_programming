#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    LastDigit = number % 10
else:
    LastDigit = ((number * -1) % 10) * -1
message = "Last digit of"
if LastDigit > 5:
    print(f"{message} {number} is {LastDigit} and is greater than 5")
elif LastDigit == 0:
    print(f"{message} {number} is {LastDigit} and is 0")
elif (LastDigit < 6) and (LastDigit != 0):
    print(f"{message} {number} is {LastDigit} and is less than 6 and not 0")
