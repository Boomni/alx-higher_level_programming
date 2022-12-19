#!/usr/bin/python3
for num1 in range(0, 9):
    for num2 in range(0, 10):
        if num1 < num2:
            if num1 < 8:
                print("{:d}{:d}".format(num1, num2), end=", ")
            else:
                print("{:d}{:d}".format(num1, num2))
