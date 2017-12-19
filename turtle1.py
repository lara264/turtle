from turtle import *
import random

t1 = Turtle()

t1.penup()
t1.goto(100, 80)
t1.pendown()
t1.speed(75)

christmas_color = ["green", "red", "blue"]

for x in range(20, 175):
    if(x%2 ==0):
        t1.color(random.choice(christmas_color))
    t1.forward(50 - 2*x)
    t1.right(10 + 2*x)


done()