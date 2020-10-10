"""
To generate random colors.
"""
import random
import math
import pygame
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
    """
    This function returns a random color in HSB format as a string.
    """
    color = '#'
    hex_list = [get_random_hex_digit() for i in range(0,6)]
    color += "".join(hex_list)
    return color

def main():
    """
    Executes if script is run as main script.
    """
    # initialize pygame module
    pygame.init()

    # create a surface on screen that has a size of 240x180
    screen = pygame.display.set_mode((240,180))

    # load and set logo (.convert() changes pixel format ie, the way color information about a specific
    # pixel is stored. If surface format isnt the same as display format, conversion will have to take place 
    # everytime, so there's significant performance increase in using .convert())
    # Correction - Convert is making it so that the icon isn't displayed properly, no clue why.
    logo = pygame.image.load('.assets\icon.jpg') # .convert()
    pygame.display.set_icon(logo)
    pygame.display.set_caption('Random color generator')

    running = True # variable controlling main loop

    # main loop
    while running:
        # event handling, gets all events from event queue
        for event in pygame.event.get():
            # only do something if event type is QUIT
            if event.type == pygame.QUIT:
                # change value of running, thereby exiting main loop
                running = False

print(random_color())
if __name__ =="__main__":
    """
    Run main function only if this module is executed as main script.
    If you import this module nothing is executed
    """
    main()