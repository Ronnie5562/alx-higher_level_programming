#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        print(number % 10, end="")
    else:
        print((number * -1) % 10, end="")
