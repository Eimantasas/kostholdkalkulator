from tkinter import *
from tkinter import ttk

 
window = Tk()
window.geometry("420x420")


navbar = ttk.Notebook(window)
tab1 = Frame(window)
tab2 = Frame(window)
tab3 = Frame(window)

navbar.add(tab1, text = "Matkaklulator")
navbar.add(tab2, text = "kalorikalkulator")

navbar.pack()

###############Næringskalkulator###############

Calories = Label(tab1, text="")
Fat = Label(tab1, text="")
Carbs = Label(tab1, text="")
Sugar = Label(tab1, text="")
Fiber = Label(tab1, text="")
Protein = Label(tab1, text="")
Salt = Label(tab1, text="")

inputBox_food = ttk.Combobox(tab1, values= ["Egg", "Rundstykker med valmue, first price", "Rema saltede cashew"])
inputBox_food.pack()

inputBox_amount = ttk.Combobox(tab1, values= ["Per 100 gram", "1 stykke eller porsjon"])
inputBox_amount.pack()

Calories.pack()
Fat.pack()
Carbs.pack()
Sugar.pack()
Fiber.pack()
Salt.pack()

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


button = Button(tab1, text= "Text", command = check)  
button.pack()

###############Kalorikalkulator###############

window.mainloop()
