from turtle import Turtle
import random

t = Turtle()
t.screen.bgcolor("black")
colors = ["red", "yellow", "purple"]
t.screen.tracer(0, 0)

colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    COLOR = (r, g, b)
    return COLOR

for x in range(100):
    t.circle(x)
    t.color(random_color())
    t.left(60)

t.screen.exitonclick()
t.screen.mainloop()