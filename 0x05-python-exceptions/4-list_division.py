#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    # Initialize a new list with zeros to store the division results
    result = [0] * list_length
    
    # Iterate over the range of the desired list length
    for i in range(list_length):
        try:
            # Try to divide the elements at the same position in both lists
            result[i] = my_list_1[i] / my_list_2[i]
        except (TypeError, ZeroDivisionError):
            # If the elements are not numbers or the division is not possible, print the appropriate message
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                print("Wrong type")
            else:
                print("Division by 0")
        except IndexError:
            # If one of the lists is too short, print the appropriate message
            print("Out of range")
        finally:
            # This block of code is always executed after the try/except blocks
            pass
    
    # Return the result list
    return (result)
