#!/usr/bin/python3
num = 122
while num != 96:
    if num % 2 == 0:
        print(chr(num), end="")
    else:
        print(chr(num - 32), end="")
     num -= 1
