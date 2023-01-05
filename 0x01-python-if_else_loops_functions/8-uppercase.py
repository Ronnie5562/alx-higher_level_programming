#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        C = ord(str[i]) > 96
        print("{}".format(chr(ord(str[i]) - 32 if C else ord(str[i]))), end="")
    print()
