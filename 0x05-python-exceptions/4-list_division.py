#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    # Initialize the result list with zeros
    result = [0] * list_length

    # Iterate through the elements of the result list
    for i in range(list_length):
        try:
            # Try to get the i-th element from each list
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]

            if not isinstance(element_1, (int, float)):
                print("wrong type")
                continue
            if not isinstance(element_2, (int, float)):
                print("wrong type")
                continue

            # Try to divide the elements
            result[i] = element_1 / element_2
        except ZeroDivisionError:
            print("division by 0")
            continue
        except IndexError:
            print("out of range")
            continue
        finally:
            pass

    return result
