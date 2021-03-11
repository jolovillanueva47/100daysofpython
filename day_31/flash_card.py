from tkinter import *
import pandas as pd
import random
import os
BACKGROUND_COLOR = "#B1DDC6"
random_word={}


# ------------------------------- GENERATE DATA FROM CSV ------------------------

if os.path.isfile("data/words_to_learn.csv"):
    data = pd.read_csv("data/words_to_learn.csv")
    word_dict=data.to_dict(orient="records")
else:
    data = pd.read_csv("data/french_words.csv")
    word_dict=data.to_dict(orient="records")

# ------------------------------- NEXT CARD -------------------------------------

def next_card():
    global random_word
    global flip_timer
    window.after_cancel(flip_timer)
    random_word=random.choice(word_dict)
    canvas.itemconfigure(card, image=front_card_img)
    canvas.itemconfigure(language, text="French", fill="black")
    canvas.itemconfigure(word, text=random_word["French"], fill="black")
    flip_timer=window.after(3000, flip_card)
# ------------------------------- FLIP CARD -------------------------------------

def flip_card():
    global random_word
    canvas.itemconfigure(language, text="English", fill="white")
    canvas.itemconfigure(word, text=random_word["English"], fill="white")
    canvas.itemconfigure(card, image=back_card_img)
# ------------------------------- CHECK BUTTON FUNCTION -------------------------

def check():
    global random_word
    word_dict.remove(random_word)
    print(len(word_dict))
    next_card()

# ------------------------------- WRONG BUTTON FUNCTION -------------------------

def wrong():
    next_card()

# ------------------------------- USER INTERFACE --------------------------------
window=Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,flip_card)


#Canvas
canvas=Canvas(width=800,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img=PhotoImage(file="images/card_front.png")
back_card_img=PhotoImage(file="images/card_back.png")
card=canvas.create_image(400,263,image=front_card_img)
language=canvas.create_text(400,150,text="French",font=("Arial",40,"italic"))
word=canvas.create_text(400,263,text="Word",font=("Arial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)


#Entries


#Buttons
wrong_img=PhotoImage(file="images/wrong.png")
check_img=PhotoImage(file="images/right.png")
wrong_btn=Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=wrong)
check_btn=Button(image=check_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=check)
wrong_btn.grid(row=1,column=0)
check_btn.grid(row=1,column=1)

next_card()

window.mainloop()
words_to_learn=pd.DataFrame(word_dict)
words_to_learn.to_csv("data/words_to_learn.csv", index=False)