def max_integer(my_list=[]):
    Max = my_list[0]
    for i in my_list:
        if i >= Max:
            Max = i
    return Max
