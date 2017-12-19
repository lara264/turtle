from turtle import *
import random

bgcolor("black")
colors = ["blue", "purple", "red", "yellow", "orange", "brown"]

colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    COLOR = (r, g, b)
    return COLOR

for x in range(300):
    pencolor(random_color())
    fd(x)
    left(59)


done()