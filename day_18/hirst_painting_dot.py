import colorgram
import random
import turtle as t

jolo=t.Turtle()
jolo.shape("arrow")
t.colormode(255)
jolo.speed("fastest")

list_of_colors=[]

def extract_colors(num_of_colors):
    colors = colorgram.extract("image.jpg", num_of_colors)
    for color in colors:
        r=color.rgb.r
        g=color.rgb.g
        b=color.rgb.b
        rgb_colors=(r,g,b)
        list_of_colors.append(rgb_colors)

def make_dot():
    color=random.choice(list_of_colors)
    jolo.color(color)
    jolo.dot(20,color)

def set_starting_position():
    jolo.penup()
    jolo.hideturtle()
    jolo.seth(225)
    jolo.forward(300)
    jolo.seth(0)

def create_dots():
    direction="left"
    for _ in range(10):
        for _ in range(10):
            make_dot()
            jolo.forward(50)
        jolo.seth(90)
        jolo.forward(50)
        if direction=="left":
            jolo.seth(180)
            direction="right"
        else:
            jolo.seth(0)
            direction="left"
        jolo.forward(50)


extract_colors(20)
set_starting_position()
create_dots()

scr=t.Screen()
scr.exitonclick()