from turtle import Turtle, Screen
import random

colors=["red","blue","green","orange"]
jolo=Turtle()
for sides in range(3,11):
    jolo.color(random.choice(colors))
    angle=360/sides
    print(sides)
    for _ in range(sides):  
        jolo.forward(100)
        jolo.right(angle)

screen=Screen()
screen.exitonclick();