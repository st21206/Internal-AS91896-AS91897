'This program is used to keep track of Items that are hired for Julies Party Hire Store'
'''from tkinter import *
from tkinter import ttk 
from pip import main'''

#Old CODING BELOW

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
#NEW CODING BELOW (New Treeview)

from tkinter import *
from tkinter import ttk 

root = Tk()
root.title('Julies Party Hire Store Item Tracker')
root.geometry('800x800')

the_programme = ttk.Treeview(root)

#Define column
the_programme['columns'] = ('Row', 'Name', 'Item', 'Quantity', 'Receipt Number')

#Format columns
the_programme.column('#0', width=0, stretch=NO)
the_programme.column('Row', anchor=W, width=120)
the_programme.column('Name', anchor=W, width=120)
the_programme.column('Item', anchor=W, width=120)
the_programme.column('Quantity', anchor=W, width=120)
the_programme.column('Receipt Number', anchor=W, width=120)

#Create headings, W = West
the_programme.heading('#0', text='', anchor=W)
the_programme.heading('Row', text='Row', anchor=W)
the_programme.heading('Name', text='Name', anchor=W)
the_programme.heading('Item', text='Item', anchor=W)
the_programme.heading('Quantity', text='Quantity', anchor=W)
the_programme.heading('Receipt Number', text='Receipt Number', anchor=W)

#Grid the programme``````````````````````````````````````````````````````````````````````````````````````````````````````
the_programme.grid(column=0, row=0)

section2 = Frame(root)
section2.grid(column=0, row=1)

#Labels
name = Label(section2, text='Name:', font='Helvetica') 
name.grid(row=0, column=0)

item = Label(section2, text='Item:', font='Helvetica')
item.grid(row=0, column=1)

quantity = Label(section2, text='Quantity:', font='Helvetica')
quantity.grid(row=0, column=2)

receipt_number = Label(section2, text='Receipt Number:', font='Helvetica')
receipt_number.grid(row=0, column=3)

delete_row = Label(section2, text='Delete Row:', font='Helvetica')
delete_row.grid(row=0, column=4)

#entries

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

'''#Creating labels and justifying
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
    Delete_Row.grid(row=1, column=1)'''
   

root.mainloop()

#NEW CODING AGAIN BELOW

'''root = Tk()
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
background=[('selected, '#347083)])'''


 

