from tkinter import *
from tkinter import ttk

 
window = Tk()
window.geometry("600x500")


navbar = ttk.Notebook(window)
tab1 = Frame(window)
tab2 = Frame(window)
tab3 = Frame(window)

navbar.add(tab1, text = "Matkaklulator")
navbar.add(tab2, text = "kalorikalkulator")
navbar.add(tab3, text = "BmiKalkulator")

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

inputBox_amount = ttk.Combobox(tab1, values= ["Per 100 gram", "1 porsjon eller pakke"])
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

        if inputBox_amount.get() == "1 porsjon eller pakke": 
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
        
        if inputBox_amount.get() == "1 porsjon eller pakke": 
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

from tkinter import *

def submit():
    weightamount = entry.get()
    heightamount = entry2.get()
    ageamount = entry3.get()
    multiplier = activity()
    gender = genderchoice()
    if weightamount.isdigit():
        if gender == "woman":
            anbefaltkalorier = (655.1 + (9.563 * int(weightamount)) + (1.850 * int(heightamount)) - (4.676 * int(ageamount))) * multiplier
        else:
            anbefaltkalorier = (66.47 + (13.75 * int(weightamount)) + (5.003 * int(heightamount)) - (6.755 * int(ageamount))) * multiplier

        label2.config(text="Din anbefalt daglig kalori inntak: " + str("%.2f"%anbefaltkalorier))
    else: anbefaltkalorier = 0

    delete()
    return anbefaltkalorier



def delete():
    entry.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

def validate_entry(text):
    return text.isdigit()

def activity():
    if (x.get()==0): #litt aktiv
        multiplier = 1.375
    elif (x.get()==1): #ikke aktiv
        multiplier = 1.2
    elif (x.get()==2): #aktiv
        multiplier = 1.7
    return multiplier

def genderchoice():
    if (x2.get()==0):
        choice = "man"
    else:
        choice = "woman"
    print(choice)
    return choice

activitylist = ["Litt Aktiv (trener 1-3 ganger i uka)", "Ikke Aktiv", "Aktiv (trener 5-7 ganger i uka)"]
genderlist = ["man", "woman"]

x = IntVar()
x2 = IntVar()

entry = Entry(tab2, #weight
              font=("Arial", 50),
              validate="key",
              validatecommand=(tab2.register(validate_entry), "%S"))

entry2 = Entry(tab2, #Height
              font=("Arial", 50),
              validate="key",
              validatecommand=(tab2.register(validate_entry), "%S"))

entry3 = Entry(tab2, #Age
              font=("Arial", 50),
              validate="key",
              validatecommand=(tab2.register(validate_entry), "%S"))

anbefaltkalorier = submit()

label = Label(tab2,
              font=("Arial", 35),
              text="Skriv inn vekten din (Kg)")

heightlabel = Label(tab2,
              font=("Arial", 35),
              text="Skriv inn høyden din (cm)")

agelabel = Label(tab2,
              font=("Arial", 35),
              text="Skriv inn alderen din (år)")

label2 = Label(tab2,
               font=("Arial", 35),
               text="Din anbefalt daglig kalori inntak: " + str(anbefaltkalorier))


submit_button = Button(tab2, 
                       text="submit",
                       command=submit)


for index in range(len(genderlist)):
    radiobutton2 = Radiobutton(tab2,
                              text=genderlist[index],
                              variable=x2,
                              value=index,
                              command=genderchoice)
    radiobutton2.pack(pady=5)

label.pack()
entry.pack(pady=25)

for index in range(len(activitylist)):
    radiobutton = Radiobutton(tab2,
                              text=activitylist[index],
                              variable=x,
                              value=index,
                              command=activity)
    radiobutton.pack()

heightlabel.pack()
entry2.pack()

agelabel.pack()
entry3.pack()

submit_button.pack()
label2.pack()

###############Kalorikalkulator###############


heightEntry = Entry(tab3)
heightEntry.pack()
heightLabel=Label(tab3, text="Høyde:")
heightLabel.place(x=70,y=1)

weightEntry = Entry(tab3)
weightEntry.pack()
weightLabel=Label(tab3, text="Kroppsvekt:")
weightLabel.place(x=70,y=30)

BMIerIkkeAltText=Label(tab3, text="Husk at hvis man har en god del muskler vil BMI ikke være like bra på å finne ut om du er overvekt eller ikke.")
BMIerIkkeAltText.pack()

BMItext = Label(tab3, text="")
BMItext.pack()

harJegFedmetext = Label(tab3, text="")
harJegFedmetext.pack()

def getHeightAndWeight() :
    height=float(heightEntry.get())
    weight=float(weightEntry.get())
    BMI = weight/((height/100)**2)
    shortBMI = ("%.2f"%BMI)
    BMItext.config(text=shortBMI)
    if (BMI < 18.5):
        harJegFedmetext.config(text='BMI under 18.5 fører ifølge FHI til økt risiko for helseproblemer.'+"\n"+'https://www.fhi.no/le/overvekt/kroppsmasseindeks-kmi-og-helse/')

    elif (BMI < 19.5):
        harJegFedmetext.config(text="Du har normal vekt, men pass på at BMI-en din ikke synker.")

    elif (BMI < 19.5):
        harJegFedmetext.config(text="Du har normal vekt, men pass på at BMI-en din ikke synker.")

    elif (BMI < 19.5):
        harJegFedmetext.config(text="Du har normal vekt, men pass på at BMI-en din ikke synker.")

    elif (BMI < 19.5):
        harJegFedmetext.config(text="Du har normal vekt, men pass på at BMI-en din ikke synker.")

    elif (BMI < 19.5):
        harJegFedmetext.config(text="Du har normal vekt, men pass på at BMI-en din ikke synker.")           


b1 = Button(tab3, text="Finn BMI-en din", command=getHeightAndWeight)
b1.pack()

window.mainloop()
