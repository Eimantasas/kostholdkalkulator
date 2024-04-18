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

window = Tk()
window.geometry("400x400")

activitylist = ["Litt Aktiv (trener 1-3 ganger i uka)", "Ikke Aktiv", "Aktiv (trener 5-7 ganger i uka)"]
genderlist = ["man", "woman"]

x = IntVar()
x2 = IntVar()

entry = Entry(window, #weight
              font=("Arial", 50),
              validate="key",
              validatecommand=(window.register(validate_entry), "%S"))

entry2 = Entry(window, #Height
              font=("Arial", 50),
              validate="key",
              validatecommand=(window.register(validate_entry), "%S"))

entry3 = Entry(window, #Age
              font=("Arial", 50),
              validate="key",
              validatecommand=(window.register(validate_entry), "%S"))

anbefaltkalorier = submit()

label = Label(window,
              font=("Arial", 35),
              text="Skriv inn vekten din (Kg)")

heightlabel = Label(window,
              font=("Arial", 35),
              text="Skriv inn høyden din (cm)")

agelabel = Label(window,
              font=("Arial", 35),
              text="Skriv inn alderen din (år)")

label2 = Label(window,
               font=("Arial", 35),
               text="Din anbefalt daglig kalori inntak: " + str(anbefaltkalorier))


submit_button = Button(window, 
                       text="submit",
                       command=submit)


for index in range(len(genderlist)):
    radiobutton2 = Radiobutton(window,
                              text=genderlist[index],
                              variable=x2,
                              value=index,
                              command=genderchoice)
    radiobutton2.pack(pady=5)

label.pack()
entry.pack(pady=25)

for index in range(len(activitylist)):
    radiobutton = Radiobutton(window,
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

window.mainloop()
