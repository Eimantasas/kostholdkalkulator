from tkinter import *
from tkinter import ttk

 
window = Tk()
window.geometry("420x420")

label = Label(window, text="asdfasdf")
label.place(x=210, y=210)

inputBox_food = ttk.Combobox(window, values= ["Egg", "Storfekjøtt", "Melk", "Kikerter"])
inputBox_food.place(x=1, y=2)

inputBox_amount = ttk.Combobox(window, values= ["Per 100 gram", "1 stykke"])
inputBox_amount.place(x=1, y=50)

def check():
    if inputBox_food.get() == "Egg":

        if inputBox_amount.get() == "Per 100 gram": 
            label.config(text="Kalorier: 155")

        if inputBox_amount.get() == "1 stykke": 
            label.config(text="Kalorier: 80")

button = Button(window, text= "Text", command = check)  
button.place(x=100, y=100)  

window.mainloop()
