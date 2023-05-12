#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    count = len(my_list)
    copy = my_list.copy()
    if idx < 0:
        return copy
    elif idx > count - 1:
        return copy
    else:
        copy[idx] = element
        return copy
