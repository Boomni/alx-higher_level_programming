#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list[:]
    if idx > -1 and idx < len(my_list):
        copy[idx] = element
    return (copy)
