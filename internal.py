'This program is used to keep track of items that are hired for Julie's Party Hire Store'

from tkinter import *
from tkinter import ttk 

#Quit Subroutine
def quit ():
    Main_Window.destroy()

def print_item_details():
    global Row, Name, Item, Quantity, Receipt No.,
    create labels as headings for printed info
    Label(Main_Window, font=('Helvetica 10 bold'),
    text='Row').grid(column=0, row=7)
     Label(Main_Window, font=('Helvetica 10 bold'),
    text='Name').grid(column=0, row=8)
     Label(Main_Window, font=('Helvetica 10 bold'),
    text='Item').grid(column=0, row=9)
     Label(Main_Window, font=('Helvetica 10 bold'),
    text='Quantity').grid(column=0, row=10)
     Label(Main_Window, font=('Helvetica 10 bold'),
    text='Receipt No.').grid(column=0, row=11)

   

Start the programming running

def main():
    global Main_Window
    global item_details, Customer_name
    Main_Window =Tk()

    Main_Window.mainloop
