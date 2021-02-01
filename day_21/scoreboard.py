from turtle import Turtle
ALIGNMENT="center"
FONT=('Arial',18,'bold')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_score()
    
    def increase_score(self):
        """
        Increase the score
        """
        self.score+=1
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT,font=FONT)
        
    
    def update_score(self):
        """
        Clears the previous text then rewrite score
        """
        self.clear()
        display=f"Score: {self.score}"
        print(display)
        self.write(display,align=ALIGNMENT, font=FONT)