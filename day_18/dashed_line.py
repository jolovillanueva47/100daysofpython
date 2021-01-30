from turtle import Turtle, Screen

jolo=Turtle()
jolo.color("blue")
jolo.shape("arrow")
for _ in range(10):
    jolo.forward(10)
    jolo.penup()
    jolo.forward(10)
    jolo.pendown()
screen=Screen()
screen.exitonclick()