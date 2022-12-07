#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for letters in my_string:
        if letters != 'c' and letters != 'C':
            string += letters
    return (string)
