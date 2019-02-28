import turtle as t
import random
from random import choice


t.speed(0)
t.hideturtle()
t.bgcolor('black')

i=0

colors = ['red','blue','orange','Green','purple']

 


while i<200:
    color = choice(colors)
    t.pencolor(color)
    t.penup()
    t.goto(0,0)
    t.forward(100)
    t.pendown()
    t.circle(100)
    t.left(2)
    i +=1
