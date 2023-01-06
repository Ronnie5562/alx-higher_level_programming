#!/usr/bin/python3
num = 122
while num != 96:
    C = num % 2
    print("{}".format(chr(num - 32) if C else chr(num)), end="")
    num -= 1
