from tkinter import *
from math import floor

window = Tk()
window.minsize(height=350,width=350)
window.title("Pomodoro Timer")
mins = 25
countdown_condition = False
once_pressed = -1

def starttimer():
    global once_pressed
    global countdown_condition
    countdown_condition = False
    once_pressed +=1
    print (once_pressed)
    
    if once_pressed == 0 or (once_pressed > 1 and (once_pressed % 2)==0):
        countdown_condition = False
        countdown(1*60)
        
    elif once_pressed == 1 or (once_pressed > 1 and (once_pressed % 2)!=0):
        countdown_condition = True
        canvas.itemconfig(timer, text="00:00")
    
def countdown(count):
    count_min = floor(count/60)
    count_sec = count % 60
    if count > 0 and countdown_condition == False:
        window.after(1000,countdown,count-1)
        canvas.itemconfig(timer, text="{}:{}".format(count_min, count_sec))



label = Label(text="Let's Start", font=("Arial", 20, "bold"))
label.pack()
canvas = Canvas(height=300, width=300)
canvas_img = PhotoImage(file="tomato.png")

canvas.create_image(150,150,image=canvas_img)
timer = canvas.create_text(150,150,text="00:00",font=("Arial",20,"bold"),fill="white")
canvas.pack()
button_img = PhotoImage(file="power1.png")

button = Button(image=button_img, highlightthickness=0, command=starttimer)
button.pack()




window.mainloop()