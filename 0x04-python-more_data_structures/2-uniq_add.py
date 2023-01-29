#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_set = set(my_list)
    res = 0
    for num in new_set:
        res += num
    return (res)