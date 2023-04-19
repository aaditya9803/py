from tkinter import *
 
window = Tk()
my_img = PhotoImage(file='tomato.png')
my_img.img = my_img
 
resized_img = my_img.subsample(2,2)
canvas = Canvas()
canvas.create_image(window.winfo_reqwidth(), window.winfo_reqheight()/2, image=resized_img)
canvas.pack()
window.mainloop()