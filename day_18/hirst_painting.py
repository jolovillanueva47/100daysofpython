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

def make_circle():
    color=random.choice(list_of_colors)
    jolo.color(color)
    jolo.begin_fill()
    jolo.circle(20)
    jolo.end_fill()

def create_circles():
    direction="left"
    for _ in range(10):
        for _ in range(10):
            make_circle()
            jolo.penup()
            jolo.forward(50)
        jolo.penup()
        jolo.seth(90)
        if direction=="left":
            jolo.forward(100)
            jolo.seth(180)
            direction="right"
        else:
            jolo.forward(25)
            jolo.seth(0)
            direction="left"
        jolo.forward(50)
        jolo.pendown()

extract_colors(20)
create_circles()

scr=t.Screen()
scr.exitonclick()