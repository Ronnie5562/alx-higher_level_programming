#!/usr/bin/python3
def no_c(my_string):
    NEW = ''
    for x in my_string:
        if x != 'c' and x != 'C':
            NEW += x
    return NEW
