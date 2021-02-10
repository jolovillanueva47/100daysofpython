from turtle import Turtle
ALIGNMENT="center"
FONT=('Arial',18,'bold')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.get_high_score()
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
        
    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
            self.new_high_score()
        self.get_high_score()
        self.score=0
        self.update_score()
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT,font=FONT)
        
    
    def update_score(self):
        """
        Clears the previous text then rewrite score
        """
        self.clear()
        display=f"Score: {self.score} High Score: {self.highscore}"
        self.write(display,align=ALIGNMENT, font=FONT)
    
    def get_high_score(self):
        with open("data.txt") as file:
            self.highscore=int(file.read())
    
    def new_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.highscore))