#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) > 96:
            print("{}".format(chr(ord(str[i]) - 32)), end="")
        else:
            print("{}".format(chr(ord(str[i]))), end="")
