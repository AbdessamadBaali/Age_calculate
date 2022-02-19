# ============= calcul age ===============
from plyer import notification
from tkinter import *
from tkinter import messagebox
# creat the main app window
root = Tk()
# change the title of the window
root.title("Abdessamad baali")
# set demensions of the window
root.geometry("400x250")
# creat a label
age_label = Label(root, text="Calculate Age",height=2, font=("Verdana", 18)).pack()
# user var
age = StringVar()
# set the input to a default valuer
age.set("00")
# creat the input for user
age_input = Entry(root, width=30, font=("Arial",16), textvariable=age).pack()

def calc():
    the_age_value = age.get()
    months = int(the_age_value) * 12
    weeks = months * 4
    days = int(the_age_value) * 365
    lines = f"""Your Age In Months Is: {months} Months
Your Age In Weeks Is: {weeks} weeks
Your Age In Days Is: {days} days"""
    messagebox.showinfo("Your Age In All Time Units",lines,)
# creat the button
btn = Button(root,font=("Arial",16), text="calcul", bg="#f90",fg="white" ,borderwidth=0, command=calc).pack()
# run the app infinitely
root.mainloop()
