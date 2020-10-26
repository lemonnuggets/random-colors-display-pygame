"""
To generate random colors.
"""
import random
import math
import pygame
WIDTH = 800
HEIGHT = 600
NUM = 50
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

def random_hsb_color():
    """
    This function returns a random color in HSB format as a string.
    """
    color = '#'
    hex_list = [get_random_hex_digit() for i in range(0,6)]
    color += "".join(hex_list)
    return color

def random_rgb_color():
    """
    This function returns a random color in HSB format as (r, g, b)
    """
    return hsb_to_rgb(random_hsb_color())

def hex_to_dec(hex_):
    """
    Converts hexadecimal number to decimal number
    """
    return int(hex_, 16)

def hsb_to_rgb(hsb):
    """
    Converts HSB color to RGB and returns value in format (r,g,b)
    """
    hsb_r = hsb[1:3]
    hsb_g = hsb[3:5]
    hsb_b = hsb[5:]

    rgb_r = hex_to_dec(hsb_r)
    rgb_g = hex_to_dec(hsb_g)
    rgb_b = hex_to_dec(hsb_b)

    return (rgb_r, rgb_g, rgb_b)

def get_median_factors_of(x):
    """
    Returns factors of given integer such that the difference between the two factors is minimum.
    """
    root = math.floor(math.sqrt(x))
    for a in range(root, 1, -1):
        if x % a == 0:
            return [a, x // a]

def draw(screen):
    """
    All the drawing stuff
    """
    factors = get_median_factors_of(NUM)
    shape_width = math.floor(WIDTH / factors[1])
    shape_height = math.floor(HEIGHT / factors[0])
    rad = min((shape_width, shape_height)) // 2
    for x in range(0, WIDTH, shape_width):
        for y in range(0, HEIGHT, shape_height):
            # pygame.draw.ellipse(screen, random_rgb_color(), (x, y, shape_width, shape_height), 3)
            pygame.draw.circle(screen, random_rgb_color(), (x + rad, y + rad), rad)

def main():
    """
    Executes if script is run as main script.
    """
    # initialize pygame module
    pygame.init()

    # create a surface on screen that has a size of 240x180
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # load and set logo (.convert() changes pixel format ie, the way color information about a
    # specific pixel is stored. If surface format isnt the same as display format, conversion
    # will have to take place everytime, so there's significant performance increase in
    # using .convert())
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                draw(screen)
                pygame.display.update()

if __name__ =="__main__":
    # Run main function only if this module is executed as main script.
    # If you import this module nothing is executed
    main()
