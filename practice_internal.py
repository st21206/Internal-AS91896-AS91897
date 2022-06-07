"""This program is so we know where camps are overnight
Need to ensure that the quit subroutine is added along with the main function which
needs to be called.
Then create the labels and buttons"""


from logging import Main_Window
from tkinter import * #Imports everything from Tkinter

#quit subroutine
def quit():
    Main_Window.destroy()

#print details of all the camps
def print_camp_details ():
    global j_names, total_entries, name_count
    name_count = 0
    Label(Main_Window, font='bold',text="Row").grid(column=0,row=7)
    Label(Main_Window, font='bold',text="Leader").grid(column=1,row=7)
    Label(Main_Window, font='bold',text="Location").grid(column=2,row=7)
    Label(Main_Window, font='bold',text="Number of Campers").grid(column=3,row=7)
    Label(Main_Window, font='bold',text="Weather").grid(column=4,row=7)

    while name_count < total_entries :
        Label(Main_Window, text=name_count).grid(column=0,row=name_count+8) 
        Label(Main_Window, text=(camp_details[name_count][0])).grid(column=1,row=name_count+8)
        Label(Main_Window, text=(camp_details[name_count][1])).grid(column=2,row=name_count+8)
        Label(Main_Window, text=(camp_details[name_count][2])).grid(column=3,row=name_count+8)
        Label(Main_Window, text=(camp_details[name_count][3])).grid(column=4,row=name_count+8)
        name_count +=  1

#add the next camper to the list
def append_name ():
    global camp_details, entry_leader,entry_location,entry_campers,entry_weather, total_entries
    if len(entry_leader.get()) != 0 :
        camp_details.append([entry_leader.get(),entry_location.get(),entry_campers.get(),entry_weather.get()])
        entry_leader.delete(0,'end')
        entry_location.delete(0,'end')
        entry_campers.delete(0,'end')
        entry_weather.delete(0,'end')
        total_entries +=  1

#delete a row from the list
def delete_row ():
    global camp_details, delete_item, total_entries, name_count
    del camp_details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0,'end')
    Label(Main_Window, text="").grid(column=0,row=name_count+7) 
    Label(Main_Window, text="").grid(column=1,row=name_count+7)
    Label(Main_Window, text="").grid(column=2,row=name_count+7)
    Label(Main_Window, text="").grid(column=3,row=name_count+7)
    Label(Main_Window, text="").grid(column=4,row=name_count+7)
    print_camp_details()

#create buttons and labels so that the GUI will have visual buttons and labels
def setup_buttons():
    global camp_details, entry_leader,entry_location,entry_campers,entry_weather, total_entries, delete_item
    Button(Main_Window, text="Quit",command=quit) .grid(column=1, row=0)
    Button(Main_Window, text="Append Details",command=append_name) .grid(column=0,row=1)
    Button(Main_Window, text="Print Details",command=print_camp_details) .grid(column=1,row=1)
    Label(Main_Window, text="Leader") .grid(column=0,row=2)
    entry_leader = Entry(Main_Window)
    entry_leader.grid(column=1,row=2)
    Label(Main_Window, text="Location") .grid(column=0,row=3)
    entry_location = Entry(Main_Window)
    entry_location.grid(column=1,row=3)
    Label(Main_Window, text="Number of Campers") .grid(column=0,row=4)
    entry_campers = Entry(Main_Window)
    entry_campers.grid(column=1,row=4)
    Label(Main_Window, text="Weather") .grid(column=0,row=5)
    entry_weather = Entry(Main_Window)
    entry_weather.grid(column=1,row=5)
    Label(Main_Window, text="Row #") .grid(column=0,row=6)
    delete_item = Entry(Main_Window)
    delete_item .grid(column=1,row=6)
    Button(Main_Window, text="Delete",command=delete_row) .grid(column=2,row=6)

#start the program running
def main():
    global Main_Window
    global camp_details, entry_name,entry_age,entry_gender, total_entries
    camp_details = []
    total_entries = 0
    Main_Window =Tk()
    setup_buttons()
    Main_Window.mainloop()
    
main()
