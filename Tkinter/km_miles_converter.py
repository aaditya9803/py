from tkinter import *
window = Tk()
window.minsize(height="400",width="600")
window.title("Convert km/Miles")


    
miles = Label(text="Enter miles", font = ("Arial",10,"bold"))
miles.grid(row=3, column= 2, pady = 20)
miles_entry = Entry(width=10)
miles_entry.grid(row = 3, column = 3)
miles_entry.focus()
km = Label(text = "In Kilometers",font = ("Arial",10,"bold"))
km.grid(row=5, column =2)

km_out = Text(height=1, width=10)
def compare_1():
    __ = miles_entry.get()
    km_out.insert(END,"{}".format(int(__)*1.60934))
def compare_2():
    __ = miles_entry.get()
    km_out.insert(END,"{}".format(int(__)*0.621371))
km_out.grid(row=5, column=3)
compare = Button(text="compare", command=compare_1)
compare.grid(row=4, column=3, pady=20)
def kmtomiles():
    km_out.delete('1.0', END)
    miles_entry.delete(0, END)
    miles.config(text = "Enter Kilometers")
    km.config(text = "In Miles")
    compare.config(command=compare_2)
def milestokm():
    km_out.delete('1.0', END)
    miles_entry.delete(0, END)
    miles.config(text="Enter miles")
    km.config(text = "In Kilometers")
    compare.config(command=compare_1)
    
    
label1 = Label(text="Choose 'km to miles' or 'miles to km'", font=("Arial",10,"bold"), pady = 10)
label1.grid(row = 1, column = 2)
checked = IntVar()
button = Radiobutton(text="Km to miles", font = ("Arial",20,"bold"),pady = 30, variable=checked, value=1, command=kmtomiles)
button.grid(row=2, column = 1)
label = Label(text="__OR__", font = ("Arial",20,"bold"))
label.grid(row = 2, column = 2)
button = Radiobutton(text="Miles to Km", font = ("Arial",20,"bold"), variable=checked, value=0, command=milestokm)
button.grid(row=2, column = 3)





window.mainloop()