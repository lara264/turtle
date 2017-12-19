from turtle import *

t1 = Turtle()

bgcolor("white")

def fibonacci():
    a = 0
    b = 1
    c = 1
    old_c = a
    for x in range(0, 20):
        t1.forward(1)
        t1.right(c - old_c)
        old_c = c
        c = a + b
        a = b
        b = c

def quarter_circle():
    t1.left(90)
    for x in range(90):
        t1.forward(1)
        t1.right(1)

#fibonacci()
quarter_circle()

done()