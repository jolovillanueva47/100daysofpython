from turtle import Turtle, Screen

jolo=Turtle()
screen=Screen()

def move_forward():
    jolo.forward(10)

screen.listen()
screen.onkey(key="space",fun=move_forward)
screen.exitonclick()
