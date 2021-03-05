import tkinter
window=tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_clicked():
    # print("I got clicked")
    my_label.config(text=input.get())

#Label
my_label=tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"]="New Text"
my_label.config(text="NEW TEXT")
my_label.grid(column=0, row=0)

#Button
button=tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1,row=1)

#New Button
new_button=tkinter.Button(text="New Button")
new_button.grid(column=2,row=0)

#Entry
input=tkinter.Entry(width=10)
# input.pack()
input.grid(column=3,row=2)

window.mainloop()