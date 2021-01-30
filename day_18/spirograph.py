import turtle as t
import random

jolo=t.Turtle()
t.colormode(255)
jolo.speed("fastest")

def random_color():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    color_tuple=(r,g,b)
    return color_tuple

def draw_spirograph(size_of_gap):
    for _ in range (int(360/size_of_gap)):
        jolo.color(random_color())
        jolo.circle(100)
        jolo.setheading(jolo.heading()+size_of_gap)

draw_spirograph(5)
screen=t.Screen()
screen.exitonclick()