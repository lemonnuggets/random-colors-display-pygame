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
    #initialize pygame module
    pygame.init()

    #load and set logo
    logo = pygame.image.load('.assets\icon.jpg')
    pygame.display.set_icon(logo)
    pygame.display.set_caption('Random color generator')
    
    #create a surface on screen that has a size of 240x180
    screen = pygame.display.set_mode((240,180))

    running = True #variable controlling main loop

    #main loop
    while running:
        #event handling, gets all events from event queue
        for event in pygame.event.get():
            #only do something if event type is QUIT
            if event.type == pygame.QUIT:
                #change value of running, thereby exiting main loop
                running = False
    
"""
    Run main function only if this module is executed as main script.
    If you import this module nothing is executed
"""

if __name__ =="__main__":
    main()
