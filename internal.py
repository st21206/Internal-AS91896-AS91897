#Main Code that functions below
#This program is used to keep track of Items that are hired for Julies Party Hire Store
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Julies Party Hire Store: Item Tracker')
root.geometry('1000x600')

program_tree = ttk.Treeview(root)

# Define Columns
program_tree['columns'] = ('Row', 'Name', 'Item', 'Quantity', 'Receipt Number')

# format the columns + phantom column
program_tree.column('#0', width=0, stretch=NO)
program_tree.column('Name', anchor=W, width=140)
program_tree.column('Row', anchor=CENTER, width=140)
program_tree.column('Item', anchor=W, width=140)
program_tree.column('Quantity', anchor=W, width=140)
program_tree.column('Receipt Number', anchor=W, width=140)

# Create Headings
program_tree.heading('#0', text='Placeholder', anchor=W)
program_tree.heading('Name', text='Name', anchor=W)
program_tree.heading('Row', text='Row', anchor=CENTER)
program_tree.heading('Item', text='Item', anchor=W)
program_tree.heading('Quantity', text='Quantity', anchor=W)
program_tree.heading('Receipt Number', text='Receipt Number', anchor=W)

# Pack to screen
program_tree.pack(pady=20)

add_frame = Frame(root)
add_frame.pack(pady=20)

# Labels
Name = Label(add_frame, text='Name')
Name.grid(row=0, column=1)

Row = Label(add_frame, text='Row')
Row.grid(row=0, column=0)

Item = Label(add_frame, text='Item')
Item.grid(row=0, column=2)

Quantity = Label(add_frame, text='Quantity')
Quantity.grid(row=0, column=3)

Receipt_Number = Label(add_frame, text='Receipt Number')
Receipt_Number.grid(row=0, column=4)

# Entry Boxes
name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

row_box = Entry(add_frame)
row_box.grid(row=1, column=1)

item_box = Entry(add_frame)
item_box.grid(row=1, column=2)

quantity_box = Entry(add_frame)
quantity_box.grid(row=1, column=3)

receipt_number_box = Entry(add_frame)
receipt_number_box.grid(row=1, column=4)

# Add record
global count
count=0


def add_record():
    global count
    program_tree.insert(parent='', index='end', iid=count, text='Placeholder', values=(name_box.get(), row_box.get(), item_box.get(), quantity_box.get(), receipt_number_box.get()))
    count += 1

    #clear the boxes
    name_box.delete(0, END)
    row_box.delete(0, END)
    item_box.delete(0, END)
    quantity_box.delete(0, END)
    receipt_number_box.delete(0, END)

#Remove all records
def remove_all():
    for record in program_tree.get_children():
        program_tree.delete(record)

# remove one selected
def remove_one():
    a = program_tree.selection()[0]
    program_tree.delete(a)

# remove many selected
def remove_many():
    a = program_tree.selection()
    for record in a:
        program_tree.delete(record)
  
# Buttons
add_record = Button(root, text='Add Record', command=add_record)
add_record.pack(pady=20)

# remove all
remove_all = Button(root, text='Remove All Records', command=remove_all)
remove_all.pack(pady=10)

# remove one
remove_one = Button(root, text='Remove One Selected', command=remove_one)
remove_one.pack(pady=10)

# remove many selected
remove_many = Button(root, text='Remove Many Selected', command=remove_many)
remove_many.pack(pady=10)

root.mainloop()

# Draft 1 Below

'''#Quit Subroutine
def quit ():
    the_programme.destroy()



root = Tk()
def callback ():
    label.config(text= 'Appended')
    label = Label(root, text = 'Detasection2s')
    label.pack()
    button = Button(root, text = 'Appended', command=callback)
    button['state'] = 'disabled'
    button['state'] = 'normal'
    button.pack()



def print_store_detasection2s():
    global Name_Count, total_entries
    Name_Count = 0
    total_entries = 0




    #create labels as headings for printed info
    Label(the_programme, font=('Helvetica 10 bold'),
    text='Row').grid(column=0, Row_Count=7)
    Label(the_programme, font=('Helvetica 10 bold'),
    text='Name').grid(column=0, Row_Count=8)
    Label(the_programme, font=('Helvetica 10 bold'),
    text='Item').grid(column=0, Row_Count=9)
    Label(the_programme, font=('Helvetica 10 bold'),
    text='Item Quantity').grid(column=0, Row_Count=10)
    Label(the_programme, font=('Helvetica 10 bold'),
    text='Receipt No.').grid(column=0, Row_Count=11)

entry = ttk.Entry(root)
entry2 = ttk.Entry(root)
entry3 = ttk.Entry(root)
entry4 = ttk.Entry(root)

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
    Label (the_programme,text= random_receipt, width =12).grid(column=0,row=1, sticky=E)
    count_items = {'count_dice':0}

def main():
    Button(the_programme, text='Quit',command=quit, width =12).grid(column=0, row=0,sticky=E)
    Button(the_programme, text ='Generate',command=generate_random, width=12).grid(column=1,row=1, sticky=E)
    the_programme.mainloop()



#Check the inputs are all valid
def check_inputs():
    #These are the global variables that are used
    global entry_item, entry_name, quantity_item, entry_receipt_number, total_entries
    entry_item = 0
    entry_name = 0
    quantity_item = 0
    entry_receipt_number = 0

    Label(the_programme, text='           ') .grid(column=2, row=0)
    Label(the_programme, text='           ') .grid(column=2, row=1)
    Label(the_programme, text='           ') .grid(column=2, row=2)
    Label(the_programme, text='           ') .grid(column=2, row=3)
    Label(the_programme, text=Name_Count).grid(column=0, Row_Count=Name_Count+8)
    Label(the_programme, text=(Item_Entries_detasection2s[Name_Count] [0])).grid(
        column=1, Row_Count=Name_Count+8)
    Label(the_programme, text=(Item_Entries_detasection2s[Name_Count] [1])).grid(
        column=2, Row_Count=Name_Count+8)
    Label(the_programme, text=(Item_Entries_detasection2s[Name_Count] [2])).grid(
        column=3, row=Name_Count+8)
    



#Start the programming running



def main():
    global the_programme
    global Item_Entries_detasection2s, Customer_Name_Count
    Item_Entries_detasection2s = 0
    Customer_Name_Count = 0

    count_items = {'count_dice':0}
    the_programme =Tk()
    main()
    root.geometry('1000x500')
    root.mainloop()
'''
#2nd Draft
'''This program is used to keep track of Items that are hired for Julies Party Hire Store

from tkinter import *
from tkinter import ttk 
import tkinter as tk

root = tk.Tk()
root.title('Julies Party Hire Store Item Tracker')
root.geometry('550x400')

the_programme = ttk.Treeview(root,selectmode='browse')

#Define column
the_programme['columns'] = ('Row', 'Name', 'Item', 'Quantity', 'Receipt Number')

#Format columns
the_programme.column('#0', width=0, stretch=NO)
the_programme.column('Row', width=80, anchor='c')
the_programme.column('Name', width=80, anchor='c')
the_programme.column('Item', width=80, anchor='c')
the_programme.column('Quantity', width=80, anchor='c')
the_programme.column('Receipt Number', anchor='c')

#Create headings, W = West
the_programme.heading('#0', text='',)
the_programme.heading('Row', text='Row')
the_programme.heading('Name', text='Name')
the_programme.heading('Item', text='Item')
the_programme.heading('Quantity', text='Quantity')
the_programme.heading('Receipt Number', text='Receipt Number')

# Name: Label/Text
l1 = tk.Label(root,  text='Name: ', width=10,anchor='c' )  
l1.grid(row=5,column=1) 

t1 = tk.Text(root,  height=1, width=20) 
t1.grid(row=5,column=2) 

# Delete: Text/Row Menu
l2 = tk.Label(root,  text='Delete: ', width=10 )  
l2.grid(row=9,column=1) 

rows = StringVar(root)
rows.set('') # default value

row1 = OptionMenu(root, rows, 'Three', 'Four', 'Five')
row1.grid(row=9,column=2)

#Item: Label/Text
l3 = tk.Label(root,  text='Item: ', width=10 )  
l3.grid(row=6,column=1) 

t3 = tk.Text(root,  height=1, width=20) 
t3.grid(row=6,column=2) 

# Quantity: Label/Text
l4 = tk.Label(root, text='Quantity: ', width=10 )
l4.grid(row=7,column=1)

t4 =tk.Text(root, height=1, width=20)
t4.grid(row=7, column=2)

# Receipt Number: Label/Text
l5= tk.Label(root, text='Receipt Number: ', width=11)
l5.grid(row=8, column=1)

t5 = tk.Text(root, height=1, width=20)
t5.grid (row=8, column=2)

# Add Record
b1 = tk.Button(root,  text='Add Record', width=10, 
               command=lambda: add_data())  
b1.grid(row=7,column=3) 
my_str = tk.StringVar()
l6 = tk.Label(root,  textvariable=my_str, width=10 )  
l6.grid(row=10,column=5) 
def add_data():
     
     my_name=t1.get('1.0',END) # read name
     my_class=rows.get()    # read class
     my_mark=t3.get('1.0',END) # read mark
     global i
     i=i+1
     the_programme.insert('','end',
                values=(i,my_name,my_class,my_mark))
     t1.delete('1.0',END)  # reset the text entry box
     t3.delete('1.0',END)  # reset the text entry box
     my_str.set('Data added ')
     t1.focus()   
     l5.after(3000, lambda: my_str.set('') ) # remove the message   

#Grid the programme
the_programme.grid(column=1, row=1, columnspan=4,padx=20,pady=20)

root.mainloop()
'''
# 3rd Draft Below
'''section2 = Frame(root)
section2.grid(column=0, row=1)

#Labels
name = Label(section2, text='Full Name:', font='Helvetica') 
name.grid(row=0, column=0)

item = Label(section2, text='Item:', font='Helvetica')
item.grid(row=0, column=1)

quantity = Label(section2, text='Quantity:', font='Helvetica')
quantity.grid(row=0, column=2)

receipt_number = Label(section2, text='Receipt Number:', font='Helvetica')
receipt_number.grid(row=0, column=3)

delete_row = Label(section2, text='Delete Row:', font='Helvetica')
delete_row.grid(row=0, column=4)

# entries

entry = ttk.Entry(section2)
entry.grid(row=1, column=0)

entry1 = ttk.Entry(section2)
entry1.grid(row=1, column=1)

entry2 = ttk.Entry(section2)
entry2.grid(row=1, column=2)

entry3 = ttk.Entry(section2)
entry3.grid(row=1, column=3)

entry4 = ttk.Entry(section2)
entry4.grid(row=1, column=4)

#buttons
add_name = Button(root, text='Print Details')
add_name.grid(column=0, row=2)

Delete = Button(root, text='Delete')
Delete.grid(column=0, row=3)

Quit = Button(root, text='Quit')
Quit.grid(column=0, row=4)

#treeview rows



#Creating labels and justifying
def create_text(self, root):
        self.textbox = Text(root, height = 10, width = 79, wrap = 'word')
        vertscroll = ttk.Scrollbar(root)
        vertscroll.config(command=self.textbox.yview)
        vertscroll.pack(side='right', fsection2l='y', expand=False)
        self.textbox.config(yscrllcommand=vertscroll.set)
        self.textbox.pack(side='left', fsection2l='both', expand=True)
        self.textbox.grid(column = 5, row = 1)
def main_content():
    Name = Label(root, text='Name:').grid(row=0, column=0)
    font=('Helvetica', 18),
    Name.grid(row=5, column=5)
    Item = Label(root, text='Item:',
    font=('Helvetica', 18),
    bd=1, relief='sunken',
    justify='left')
    Item.grid(row=1, column=1)
    Quantity = Label(root, text='Quantity:',
    font=('Helvetica', 18),
    bd=1, relief='sunken',
    justify='left')
    Quantity.grid(row=2, column=2)
    Receipt_Number = Label(root, text='Receipt Number:',
    font=('Helvetica', 18),
    bd=1, relief='sunken',
    justify='left')
    Receipt_Number.grid(row=3, column=3)
    Delete_Row = Label(root, text='Delete Row:',
    font=('Helvetica', 18),
    bd=1, relief='sunken',
    justify='left')
    Delete_Row.grid(row=1, column=1)
   '''
# 4th Draft Below
'''
root = Tk()
root.title('Julies Party Hire Store Item Tracker')
root.geometry('100x500')


#theme
style = ttk.Style()
style.theme_use('default')

#configuring treeview colours
style.configure('Treeview',
background ='#D3D3D3',
foreground ='black',
rowheight =25,
fieldbackground='#D3D3D3')

#Change selected colour
style.map('Treeview',
background=[('selected, '#347083)])
'''