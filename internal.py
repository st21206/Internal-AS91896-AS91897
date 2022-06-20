'This program is used to keep track of Item_Entriess that are hired for Julie's Party Hire Store'



from tkinter import *
from tkinter import ttk 



#Quit Subroutine
def quit ():
    main_window.destroy()



def print_store_details():
    global Name_Count, total_entries
    Name_Count = 0



    #create labels as headings for printed info
    Label(main_window, font=('Helvetica 10 bold'),
    text='Row').grid(column=0, Row_Count=7)
    Label(main_window, font=('Helvetica 10 bold'),
    text='Name').grid(column=0, Row_Count=8)
    Label(main_window, font=('Helvetica 10 bold'),
    text='Item').grid(column=0, Row_Count=9)
    Label(main_window, font=('Helvetica 10 bold'),
    text='Item Quantity').grid(column=0, Row_Count=10)
    Label(main_window, font=('Helvetica 10 bold'),
    text='Receipt No.').grid(column=0, Row_Count=11)



#Check the inputs are all valid
def check_inputs():
    #These are the global variables that are used
    global entry_item, entry_name, quantity_item, entry_receipt_no., total_entries
    input_check = 0
    Label(main_window, text='           ') .grid(column=2, row=0)
    Label(main_window, text='           ') .grid(column=2, row=1)
    Label(main_window, text='           ') .grid(column=2, row=2)
    Label(main_window, text='           ') .grid(column=2, row=3)
    
    
while Name_Count < total_entries:
    Label(main_window, text=Name_Count).grid(column=0, Row_Count=Name_Count+8)
    Label(main_window, text=(Item_Entries[Name_Count] [0])).grid(
        column=1, Row_Count=Name_Count+8)
    Label(main_window, text=(Item_Entries[Name_Count] [1])).grid(
        column=2, Row_Count=Name_Count+8)
    Label(main_window, text=(Item_Entries[Name_Count] [2])).grid(
        column=3, row=Name_Count+8)
    )



#Start the programming running



def main():
    global main_window
    global Item_Entries_details, Customer_Name_Count
    main_window =Tk()



    main_window.mainloop
