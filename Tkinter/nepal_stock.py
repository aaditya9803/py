from unicodedata import name
import requests
from tkinter import *
from tkinter import ttk

window = Tk()
window.minsize(height=350,width=350)
window.title("My Stocks")
frame = Frame()
frame.pack()

# end_point = "https://nepse-data-api.herokuapp.com/data/todaysprice"
# response = requests.get(end_point)
# response.raise_for_status()
# data = response.json()

data = [{"companyName":"10 Prime Debenture 2088", "noOfTransactions":4},
        {"companyName":"10 Sunrise Debenture 2080","noOfTransactions":1}]

my_table = ttk.Treeview(frame)
my_table['columns']=('id','Name')
my_table.column("#0", width=0,  stretch=NO)
my_table.heading("#0",text="",anchor=CENTER)

my_table.column("id",anchor=CENTER, width=80)
my_table.heading("id",text="Id",anchor=CENTER)

my_table.column("Name",anchor=CENTER,width=80)
my_table.heading("Name",text="Name",anchor=CENTER)

# my_table.insert(parent='',index='end',iid=0,text='', values=('1','Ninja'))
# my_table.insert(parent='',index='end',iid=1,text='', values=('2','Ranger'))

    
class Insert_table:
    def __init__(self, name, i):
        self.name = name
        self.number = i
        self.i = i
    def add(self):
        my_table.insert(parent='',index='end',iid= i ,text='', values=(self.i, self.name))
i=0
for datas in data:
    # print(datas['companyName'])
    a = datas['companyName']
    Insert_table(a,i).add()
    i+=1








my_table.pack()











window.mainloop()