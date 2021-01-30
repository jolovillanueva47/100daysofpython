from turtle import Turtle, Screen

jolo_the_turtle=Turtle()
jolo_the_turtle.shape("turtle")
jolo_the_turtle.color("LightPink")

for _ in range(4):
    jolo_the_turtle.forward(100)
    jolo_the_turtle.right(90)


screen=Screen()
screen.exitonclick()