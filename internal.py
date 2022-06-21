'This program is used to keep track of Items that are hired for Julies Party Hire Store'
from tkinter import *
from tkinter import ttk 


from pip import main

#Old CODING BELOW

"""#Quit Subroutine
def quit ():
    main_window.destroy()



root = Tk()
def callback ():
    label.config(text= 'Appended')
    label = Label(root, text = 'Details')
    label.pack()
    button = Button(root, text = 'Appended', command=callback)
    button['state'] = 'disabled'
    button['state'] = 'normal'
    button.pack()



def print_store_details():
    global Name_Count, total_entries
    Name_Count = 0
    total_entries = 0




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

entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)
entry3 = ttk.Entry(root, width=30)
entry4 = ttk.Entry(root, width=30)

entry.insert(0, 'Please enter your name')
entry2.insert(0, 'Please enter the name of the item')
entry3.insert(0, 'Please enter the quantity of the item')
entry4.insert(0, 'Please enter the receipt number')

button = ttk.Button(root, text='Enter')
lbltitle = ttk.Label(text='Julies Party Hire Tracker', font=(('Helvetica 20 bold')))
lblname = ttk.Label(text='Name:')
lblitem = ttk.Label(text='Item:')
lblquantity = ttk.Label(text='Quantity:')
lblreceipt_number = ttk.Label(text='Receipt Number:')

lbltitle.grid(row=0, column=0)
lblname.grid(row=3, column=1, sticky=W)
lblitem.grid(row=6, column=2, sticky=W)
lblquantity.grid(row=9, column=3, sticky=W)
lblreceipt_number.grid(row=12, column=4, sticky=W)

entry.grid(row=3, column=2)
entry2.grid(row=6, column=3)
entry3.grid(row=9, column=4)
entry4.grid(row=12, column=5)
button.grid(row=15, column=6, sticky=E, pady=5)



#Generating random receipt number
def generate_random():
    count_items['generate receipt'] +=1
    LOW_NUMBER = 000000
    HIGH_NUMBER = 999999
    random_receipt = random.randint (LOW_NUMBER, HIGH_NUMBER)
    Label (main_window,text= random_receipt, width =12).grid(column=0,row=1, sticky=E)
    count_items = {'count_dice':0}

def main():
    Button(main_window, text='Quit',command=quit, width =12).grid(column=0, row=0,sticky=E)
    Button(main_window, text ='Generate',command=generate_random, width=12).grid(column=1,row=1, sticky=E)
    main_window.mainloop()



#Check the inputs are all valid
def check_inputs():
    #These are the global variables that are used
    global entry_item, entry_name, quantity_item, entry_receipt_number, total_entries
    entry_item = 0
    entry_name = 0
    quantity_item = 0
    entry_receipt_number = 0

    Label(main_window, text='           ') .grid(column=2, row=0)
    Label(main_window, text='           ') .grid(column=2, row=1)
    Label(main_window, text='           ') .grid(column=2, row=2)
    Label(main_window, text='           ') .grid(column=2, row=3)
    Label(main_window, text=Name_Count).grid(column=0, Row_Count=Name_Count+8)
    Label(main_window, text=(Item_Entries_details[Name_Count] [0])).grid(
        column=1, Row_Count=Name_Count+8)
    Label(main_window, text=(Item_Entries_details[Name_Count] [1])).grid(
        column=2, Row_Count=Name_Count+8)
    Label(main_window, text=(Item_Entries_details[Name_Count] [2])).grid(
        column=3, row=Name_Count+8)
    



#Start the programming running



def main():
    global main_window
    global Item_Entries_details, Customer_Name_Count
    Item_Entries_details = 0
    Customer_Name_Count = 0

    count_items = {'count_dice':0}
    main_window =Tk()
    main()
    root.geometry('1000x500')
    root.mainloop()
"""
#NEW CODING BELOW

from tkinter import *
from tkinter import ttk 

root = Tk()
root.title('Julies Party Hire Store Item Tracker')
root.geometry('500x500')

main_window = ttk.Treeview(root)

#Define column
main_window['columns'] = ('Row', 'Name', 'Item', 'Quantity', 'Receipt Number')

#Format columns
main_window.column('#0', width=0, stretch=NO)
main_window.column('Row', anchor=W, width=120)
main_window.column('Name', anchor=W, width=120)
main_window.column('Item', anchor=W, width=120)
main_window.column('Quantity', anchor=W, width=120)
main_window.column('Receipt Number', anchor=W, width=120)

#Create headings, W = West
main_window.heading('#0', text='', anchor=W)
main_window.heading('Row', text='Row', anchor=W)
main_window.heading('Name', text='Name', anchor=W)
main_window.heading('Item', text='Item', anchor=W)
main_window.heading('Quantity', text='Quantity', anchor=W)
main_window.heading('Receipt Number', text='Receipt Number', anchor=W)

#Pack to the screen
main_window.pack(pady=20)

root.mainloop()