from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_lbl=Label(text="Score: 0",bg=THEME_COLOR,foreground="white")
        self.score_lbl.grid(row=0,column=1)
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text=self.canvas.create_text(150,125,text="Amazon acquired Twitch",font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.true_img=PhotoImage(file="images/true.png")
        self.false_img=PhotoImage(file="images/false.png")
        self.true_btn=Button(image=self.true_img,highlightthickness=0)
        self.false_btn=Button(image=self.false_img,highlightthickness=0)
        self.true_btn.grid(row=2,column=0)
        self.false_btn.grid(row=2,column=1)
        self.window.mainloop()