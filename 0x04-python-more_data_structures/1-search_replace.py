#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list
    for num in range(len(new_list)):
       if new_list[num] == search:
           new_list[num] = replace
    return new_list
