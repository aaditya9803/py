from tkinter import *
windows = Tk()
windows.title("Hello world")
windows.minsize(height=600,width=400)
windows.maxsize(height=600,width=600)
my_label = Label(text ="hello there", font = ("Arial",24,"bold"))
my_label.pack(side = "top")
def button_clicked():
    new_text = input.get()
    my_label['text'] = new_text
    
button = Button(text="click me", command=button_clicked)
button.pack()
    
input = Entry(width=20)
input.pack()
    
windows.mainloop()
