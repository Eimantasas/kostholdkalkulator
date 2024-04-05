from tkinter import *
from tkinter import ttk

 
window = Tk()
window.geometry("420x420")

Calories = Label(window, text="")
Fat = Label(window, text="asdfasdf")
Carbs = Label(window, text="")
Sugar = Label(window, text="")
Fiber = Label(window, text="")
Protein = Label(window, text="")
Salt = Label(window, text="")

Calories.place(x=210, y=210)
Fat.place(x=210, y=230)
Carbs.place(x=210, y=250)
Sugar.place(x=210, y=270)
Fiber.place(x=210, y=290)
Salt.place(x=210, y=310)

inputBox_food = ttk.Combobox(window, values= ["Egg", "Storfekjøtt", "Melk", "Kikerter", "Rundstykker med valmue, first price"])
inputBox_food.place(x=1, y=2)

inputBox_amount = ttk.Combobox(window, values= ["Per 100 gram", "1 stykke"])
inputBox_amount.place(x=1, y=50)

def check():
    if inputBox_food.get() == "Egg":

        if inputBox_amount.get() == "Per 100 gram": 
            Calories.config(text="Kalorier: 155")

        if inputBox_amount.get() == "1 stykke": 
            Calories.config(text="Kalorier: 80")
    
    if inputBox_food.get() == "Rundstykker med valmue, first price":
        
        if inputBox_amount.get() == "Per 100 gram": 
            Calories.config(text="Kalorier: 274")
            Fat.config(text="Fett: 5,2 gram")
            Carbs.config(text="Karbohydrater: 46,2 gram")
            Sugar.config(text="Hvorav sukkerarter: 1,0 gram")
            Fiber.config(text="Kostfiber: 2,6")
            Protein.config(text="Proteiner: 9,1")
            Salt.config(text="Salt: 0,9 gram")
        
        if inputBox_amount.get() == "Per 100 gram": 
            Calories.config(text="Kalorier: 164")
            Fat.config(text="Fett: 3,2 gram")
            Carbs.config(text="Karbohydrater: 27,7 gram")
            Sugar.config(text="Hvorav sukkerarter: 0,6 gram")
            Fiber.config(text="Kostfiber: 1,5")
            Protein.config(text="Proteiner:5,5")
            Salt.config(text="Salt: 0,5 gram")


button = Button(window, text= "Text", command = check)  
button.place(x=100, y=100)  

window.mainloop()
