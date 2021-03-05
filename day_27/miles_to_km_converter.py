import tkinter

window=tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)

def convert():
    value_label.config(text=str(float(input.get())*1.609344))

input=tkinter.Entry(width=10,text="0")
input.insert(tkinter.END,"0")
input.grid(row=0,column=1)

miles_label=tkinter.Label(text="Miles")
miles_label.grid(row=0,column=2)

equate_label=tkinter.Label(text="is equal to")
equate_label.grid(row=1,column=0)

value_label=tkinter.Label(text="0")
value_label.grid(row=1,column=1)

km_label=tkinter.Label(text="Km")
km_label.grid(row=1,column=2)

calculate_button=tkinter.Button(text="Calculate", command=convert)
calculate_button.grid(row=2,column=1)

window.mainloop()