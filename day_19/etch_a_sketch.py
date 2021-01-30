from turtle import Turtle, Screen

jolo=Turtle()
screen=Screen()

def move_forward():
    jolo.forward(10)

def move_backward():
    jolo.backward(10)

def turn_left():
    jolo.left(1)

def turn_right():
    jolo.right(1)

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(jolo.clear,"c")
screen.onkey(jolo.reset,"r")
screen.exitonclick()