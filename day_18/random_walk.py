import random
import turtle as t

random_direction=[0,90,180,270]
#colors=["red","blue","green","orange"]
jolo=t.Turtle()
t.colormode(255)
jolo.pensize(10)
jolo.speed(0)

def random_color():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    color_tuple=(r,g,b)
    return color_tuple

def walk():
    jolo.right(random.choice(random_direction))
    jolo.forward(50)

for _ in range(200):
    jolo.color(random_color())
    walk()
    
screen=t.Screen()
screen.exitonclick()