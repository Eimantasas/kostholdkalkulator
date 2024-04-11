from tkinter import *

def submit():
    weightamount = entry.get()
    kalorierpergram = activity()
    if weightamount.isdigit():
        anbefaltkalorier = int(weightamount) * kalorierpergram
        label2.config(text="Din anbefalt daglig kalori inntak: " + str(anbefaltkalorier))
    else: anbefaltkalorier = 0

    delete()
    return anbefaltkalorier



def delete():
    entry.delete(0, END)

def validate_entry(text):
    return text.isdigit()

def activity():
    kalorierpergram = 0
    if (x.get()==0): #aktiv
        kalorierpergram = 35
    elif (x.get()==1): #ikke aktiv
        kalorierpergram = 29
    return kalorierpergram


window = Tk()
window.geometry("400x400")

activitylist = ["Aktiv", "Ikke Aktiv"]

x = IntVar()

entry = Entry(window,
              font=("Arial", 50),
              validate="key",
              validatecommand=(window.register(validate_entry), "%S"))

anbefaltkalorier = submit()

label = Label(window,
              font=("Arial", 35),
              text="Skriv inn vekten din")

label2 = Label(window,
               font=("Arial", 35),
               text="Din anbefalt daglig kalori inntak: " + str(anbefaltkalorier))


submit_button = Button(window, 
                       text="submit",
                       command=submit)

label.pack(pady=25)
entry.pack(pady=25)

for index in range(len(activitylist)):
    radiobutton = Radiobutton(window,
                              text=activitylist[index],
                              variable=x,
                              value=index,
                              command=activity)
    radiobutton.pack()

submit_button.pack()
label2.pack()

window.mainloop()