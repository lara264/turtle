from turtle import *
import random

#custom color
# LIGHTBLUE = (0, 191, 255)
#colormode(255)
#pencolor(LIGHTBLUE)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colormode(255)
    COLOR = (r, g, b)
    return COLOR

pencolor(random_color())

done()