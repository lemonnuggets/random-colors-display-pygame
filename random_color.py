"""
To generate random colors.
"""
import random
import math
import pygame
def random_color():
    """
    This function returns a random color in HSB format.
    """
    color = '#'
    for i in range(0,6):
        next_val = math.floor(random.random() * 16) 
        if next_val == 16:
            next_val -= 1

        if next_val < 10:
            color += str(next_val)
        elif next_val == 10:
            color += 'A'
        elif next_val == 11:
            color += 'B'
        elif next_val == 12:
            color += 'C'
        elif next_val == 13:
            color += 'D'
        elif next_val == 14:
            color += 'E'
        elif next_val == 15:
            color += 'F'

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

if __name__ =="__main__":
    """
    Run main function only if this module is executed as main script.
    If you import this module nothing is executed
    """
    main()
