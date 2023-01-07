def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        newS = my_list.copy()
        newS[idx] = element
        return newS
