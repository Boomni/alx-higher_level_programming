#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    if (my_list == []):
        return (0)
    for i in my_list:
        print(i)
        result += i
    return (result)
