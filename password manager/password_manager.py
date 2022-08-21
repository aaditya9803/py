from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


def save():
    website = website_entry.get()
    email = id_entry.get()
    password = password_entry.get()
    if len(email) == 0 or len(password)==0:
        messagebox.askokcancel(title="Incorrect info", message="Email/Password cannot be empty")
    else:
        istrue = messagebox.askokcancel(title="check info", message="Are your information correct? \n Email: {}\n Password:{}".format(email,password))
        if istrue:
            with open("password manager/data.txt","a") as data_file:
                data_file.write("{} | {} | {}\n".format(website,email,password))
    password_entry.delete(0,END)
    id_entry.delete(0,END)
    website_entry.delete(0,END)
    website_entry.focus()
    
    
def fill_password():
    b = generate_pass()
    password_entry.delete(0,END)
    password_entry.insert(0,b)
    
    
def generate_pass():
    letter = cap_letter = number = symbol = 3
    sym1 = sym2 = lett1 = lett2 = num1 = 0
    symbol1= []
    a = []
    letter1=[]
    number1=[]
    cap_letter1=[]
    for sym1 in range(32, 48):
        symbol1.append(chr(sym1))
    for sym2 in range(58, 65):
        symbol1.append(chr(sym2))
    for lett1 in range(97, 123):
        letter1.append(chr(lett1))
    for lett2 in range(65, 91):
        cap_letter1.append(chr(lett2))
    for num1 in range(48, 58):
        number1.append(chr(num1))
    # print ("here\n {} \n {} \n {} \n {}".format(symbol1, letter1, cap_letter1, number1))

    letters = random.choices(letter1, k=int(letter))
    symbols = random.choices(symbol1, k = int(symbol))
    numbers = random.choices(number1, k = int(number))
    cap_letters = random.choices(cap_letter1, k = int(cap_letter))
    a = letters + symbols + numbers + cap_letters
    random.shuffle(a) 
    b = ''.join(a)
    return b

canvas = Canvas(height=200, width=200)
canvas_img = PhotoImage(file="password manager/logo.png")
canvas.create_image(100,100,image=canvas_img)
canvas.grid(row=0,column=1, sticky=W)

website_label = Label(text="Website")
website_label.grid(row=1,column=0)
id_label = Label(text="Email/Username")
id_label.grid(row=2,column=0)
password_label = Label(text="Password")
password_label.grid(row=3,column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
id_entry = Entry(width=35)
id_entry.grid(row=2,column=1,columnspan=2)
password_entry = Entry(width=35)
password_entry.grid(row=3,column=1,columnspan=2)

generate_password = Button(text="Generate Password",command=fill_password)
generate_password.grid(row=4, column=1)
add_button = Button(text="Add",command=save)
add_button.grid(row=4,column=1, columnspan=2, sticky=E)


window.mainloop()