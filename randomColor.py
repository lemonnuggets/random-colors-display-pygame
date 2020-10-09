import math
import random
def randomColor():
    color = '#'
    for i in range(0,6):
        nextVal = math.floor(random.random() * 16) 
        if nextVal == 16:
            nextVal -= 1
        
        if nextVal < 10:
            color += str(nextVal)
        elif nextVal == 10:
            color += 'A'
        elif nextVal == 11:
            color += 'B'
        elif nextVal == 12:
            color += 'C'
        elif nextVal == 13:
            color += 'D'
        elif nextVal == 14:
            color += 'E'
        elif nextVal == 15:
            color += 'F'
    return color

print(randomColor())
    
