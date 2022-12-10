#!/usr/bin/python3
def multiply_by_2(my_dict):
    return dict(zip(my_dict.keys(), (i * 2 for i in my_dict.values())))
