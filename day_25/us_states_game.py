import turtle
import pandas as pd
screen=turtle.Screen()
screen.title("US States Game")
screen.setup(width=725,height=491)
img="blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
data=pd.read_csv("50_states.csv")
states=data.state.to_list()
turtle_writer=turtle.Turtle()
turtle_writer.hideturtle()
states_guessed=[]
while len(states_guessed)<50:
    title_fmt=f"{len(states_guessed)}/50 States Correct"
    answer_state=screen.textinput(title=title_fmt, prompt="What's the name of the state?").title()
    if answer_state == "Exit":
        break
    if answer_state in states and answer_state not in states_guessed:
        x=int(data[data.state==answer_state].x)
        y=int(data[data.state==answer_state].y)
        turtle_writer.penup()
        turtle_writer.goto(x,y)
        turtle_writer.write(answer_state)
        states_guessed.append(answer_state)
#turtle.mainloop()
states_not_guessed=[]
for state in states:
    if state not in states_guessed:
        states_not_guessed.append(state)
states_dict={
    "States": states_not_guessed
}
states_to_learn=pd.DataFrame(states_dict)
states_to_learn.to_csv("states_to_learn.csv")