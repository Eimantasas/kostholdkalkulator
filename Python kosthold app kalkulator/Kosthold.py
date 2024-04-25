from tkinter import *
from tkinter import ttk

 
window = Tk()
window.geometry("500x700")
window.resizable(False, False)


navbar = ttk.Notebook(window)
tab1 = Frame(window)
tab2 = Frame(window)
tab3 = Frame(window)

navbar.add(tab1, text = "Matkaklulator")
navbar.add(tab2, text = "kalorikalkulator")
navbar.add(tab3, text = "BMI kalkulator")

navbar.pack()

###############Næringskalkulator###############

Calories = Label(tab1, text="")
Fat = Label(tab1, text="")
Carbs = Label(tab1, text="")
Sugar = Label(tab1, text="")
Fiber = Label(tab1, text="")
Protein = Label(tab1, text="")
Salt = Label(tab1, text="")

inputBox_food = ttk.Combobox(tab1, values= ["Egg", "Rundstykker med valmue, first price", "Rema saltede cashew"], font=("Arial", 25))
inputBox_food.pack()

inputBox_amount = ttk.Combobox(tab1, values= ["Per 100 gram", "1 stykke eller porsjon"], font=("Arial", 25))
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
            Calories.config(text="Kalorier: 155", font=("Arial", 25))

        if inputBox_amount.get() == "1 stykke": 
            Calories.config(text="Kalorier: 80", font=("Arial", 25))
    
    if inputBox_food.get() == "Rundstykker med valmue, first price":
        
        if inputBox_amount.get() == "Per 100 gram":
            Calories.config(text="Kalorier: 274", font=("Arial", 25))
            Fat.config(text="Fett: 5,2 gram", font=("Arial", 25))
            Carbs.config(text="Karbohydrater: 46,2 gram", font=("Arial", 25))
            Sugar.config(text="Hvorav sukkerarter: 1,0 gram", font=("Arial", 25))
            Fiber.config(text="Kostfiber: 2,6", font=("Arial", 25))
            Protein.config(text="Proteiner: 9,1", font=("Arial", 25))
            Salt.config(text="Salt: 0,9 gram", font=("Arial", 25))
        
        if inputBox_amount.get() == "Per 100 gram": 
            Calories.config(text="Kalorier: 164", font=("Arial", 25))
            Fat.config(text="Fett: 3,2 gram", font=("Arial", 25))
            Carbs.config(text="Karbohydrater: 27,7 gram", font=("Arial", 25))
            Sugar.config(text="Hvorav sukkerarter: 0,6 gram", font=("Arial", 25))
            Fiber.config(text="Kostfiber: 1,5", font=("Arial", 25))
            Protein.config(text="Proteiner:5,5", font=("Arial", 25))
            Salt.config(text="Salt: 0,5 gram", font=("Arial", 25))


button = Button(tab1, text= "Text", command = check)  
button.pack()

###############Kalorikalkulator###############
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

        label2.config(text="Din daglige tilnærmede anbefalte kalori inntak: \n" + str("%.2f"%anbefaltkalorier))
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
    return choice

activitylist = ["Litt Aktiv (trener 1-3 ganger i uka)", "Ikke Aktiv", "Aktiv (trener 5-7 ganger i uka)"]
genderlist = ["man", "woman"]


#radiobutton variabler
x = IntVar()
x2 = IntVar()

#tallvariabler
proteinval = IntVar()
fettval = IntVar()
carbsval = IntVar()

entry = Entry(tab2, #weight
              font=("Arial", 25),
              validate="key",
              validatecommand=(window.register(validate_entry), "%S"))

entry2 = Entry(tab2, #Height
              font=("Arial", 25),
              validate="key",
              validatecommand=(window.register(validate_entry), "%S"))

entry3 = Entry(tab2, #Age
              font=("Arial", 25),
              validate="key",
              validatecommand=(window.register(validate_entry), "%S"))

anbefaltkalorier = submit()

label = Label(tab2,
              font=("Arial", 25),
              text="Skriv inn vekten din (Kg)")

heightlabel = Label(tab2,
              font=("Arial", 25),
              text="Skriv inn høyden din (cm)")

agelabel = Label(tab2,
              font=("Arial", 25),
              text="Skriv inn alderen din (år)")

label2 = Label(tab2,
               font=("Arial", 25),
               text="Din anbefalt daglig kalori inntak: \n" + str(anbefaltkalorier))


submit_button = Button(tab2, 
                       text="submit",
                       command=submit)


for index in range(len(genderlist)):
    radiobutton2 = Radiobutton(tab2,
                              text=genderlist[index],
                              variable=x2,
                              value=index,
                              command=genderchoice,
                              font=("Arial", 20))
    radiobutton2.pack(pady=5)

label.pack(pady=(20, 0))
entry.pack(pady=(0, 25))

for index in range(len(activitylist)):
    radiobutton = Radiobutton(tab2,
                              text=activitylist[index],
                              variable=x,
                              value=index,
                              command=activity,
                              font=("Arial", 20))
    radiobutton.pack()

heightlabel.pack(pady=(25, 0))
entry2.pack()

agelabel.pack(pady=(20, 0))
entry3.pack()

submit_button.pack()
label2.pack(pady=(20, 15))

###############Kalorikalkulator###############


heightEntry = Entry(tab3, font=("Arial", 15))
heightEntry.pack(pady=(20, 0))
heightLabel=Label(tab3, text="Høyde (cm):", font=("Arial", 15))
heightLabel.place(x=0,y=20)

weightEntry = Entry(tab3, font=("Arial", 15))
weightEntry.pack(pady=(20, 0))
weightLabel=Label(tab3, text="Vekt (KG):", font=("Arial", 15))
weightLabel.place(x=12,y=70)

BMIerIkkeAltText=Label(tab3, text="Husk at hvis man har en god del \n muskler vil BMI ikke være like bra \n på å finne ut om du er overvekt eller \n ikke.", font=("Arial", 20))
BMIerIkkeAltText.pack(pady=(20, 0))

BMItext = Label(tab3, text="")
BMItext.pack(pady=(20, 0))

harJegFedmetext = Label(tab3, text="")
harJegFedmetext.pack()

def getHeightAndWeight() :
    height=float(heightEntry.get())
    weight=float(weightEntry.get())
    BMI = weight/((height/100)**2)
    shortBMI = ("%.2f"%BMI)
    BMItext.config(text=shortBMI, font=("arial", 40))
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
