"This program is used to keep track of items that are hired for Julie's Party Hire Store"

from tkinter import *
from tkinter import ttk 

#Quit Subroutine
def quit ():
    Main_Window.destroy()

def print_item_details():
    global Customer_name, Receipt_number, Item, Item_quantity
    Customer_name = 0
    Receipt_number = 0
    Item = 0
    Item_quantity = 0
    #create labels as headings for printed info
    Label(Main_Window, font='bold', text='Row').grid(column=0,row=20)
    Label(Main_Window, font='bold', text='Name').grid(column=1,row=20)
    Label(Main_Window, font='bold', text='Item').grid(column=2,row=20)
    Label(Main_Window, font='bold', text='Quantity').grid(column=3,row=20)
    Label(Main_Window, font='bold', text='Receipt No.').grid(column=4,row=20)

#Start the programming running

def main():
    global Main_Window
    global item_details, Customer_name
    Main_Window =Tk()
    setup_buttons()
    Main_Window.mainloop

root=tk()

root.geometry('500x750')

root.mainloop()