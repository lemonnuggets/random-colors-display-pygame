import math
import random
def get_random_hex_digit():
    """
    Returns a random hex digit as a string (0 - F)
    """
    random_binary_digit = math.floor(random.random() * 16) 
    if random_binary_digit == 16:
        random_binary_digit -= 1
    
    if random_binary_digit < 10:
        return str(random_binary_digit)
    elif random_binary_digit == 10:
        return 'A'
    elif random_binary_digit == 11:
        return 'B'
    elif random_binary_digit == 12:
        return 'C'
    elif random_binary_digit == 13:
        return 'D'
    elif random_binary_digit == 14:
        return 'E'
    elif random_binary_digit == 15:
        return 'F'

def random_color():
    color = '#'
    hex_list = [get_random_hex_digit() for i in range(0,6)]
    color += "".join(hex_list)
    return color

print(random_color())
    
