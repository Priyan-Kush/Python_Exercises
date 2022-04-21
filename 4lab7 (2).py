# basic form to get multiple contact details using tkinter

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Contact Form")
root.geometry("600x400")
frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=1, row=0, sticky=(N, W, E, S))
contactListLabel = ttk.Label(frame, text="Contact List")
contactListLabel.grid(column=1, row=0, sticky=N)
contactListTextArea = Text(frame, width=30, height=10)
contactListTextArea.grid(column=1, row=1, sticky=(W, E),rowspan=7)
displayContactButton = ttk.Button(frame, text="Display Contact")
displayContactButton.grid(column=1, row=8, sticky= N)
NewContactLabel = ttk.Label(frame, text="New Contact")
NewContactLabel.grid(column=3, row=0, sticky=N)
firstNameLabel = ttk.Label(frame,text= "First Name")
firstNameLabel.grid(column=2, row=1, sticky=W)
firstName = ttk.Entry(frame)
firstName.grid(column=3, row=1, sticky=(W, E))
lastNameLabel = ttk.Label(frame,text= "Last Name")
lastNameLabel.grid(column=2, row=2, sticky=W)
lastName = ttk.Entry(frame)
lastName.grid(column=3, row=2, sticky=(W, E))
phoneLabel = ttk.Label(frame,text= "Phone")
phoneLabel.grid(column=2, row=3, sticky=W)
phone = ttk.Entry(frame)
phone.grid(column=3, row=3, sticky=(W, E))
friendCheckBox = ttk.Checkbutton(frame, text="Friend")
friendCheckBox.grid(column=3, row=4, sticky=W)
emailLabel = ttk.Label(frame,text= "Email")
emailLabel.grid(column=2, row=5, sticky=W)
email = ttk.Entry(frame)
email.grid(column=3, row=5, sticky=(W, E))
birthdayLabel = ttk.Label(frame,text= "Birthday")
birthdayLabel.grid(column=2, row=6, sticky=W)
birthday = ttk.Entry(frame)
birthday.grid(column=3, row=6, sticky=(W, E))
addContactButton = ttk.Button(frame, text="Add Contact")
addContactButton.grid(column=3, row=8, sticky=(W, E))
lastNameSearchLabel = ttk.Label(frame,text= "Last Name")
lastNameSearchLabel.grid(column=0, row=9, sticky=W)
lastNameSearch = ttk.Entry(frame)
lastNameSearch.grid(column=1, row=9, sticky=(W, E))
resultLabel = ttk.Label(frame,text= "Result:")
resultLabel.grid(column=3, row=9, sticky=W)
last_firstLabel = ttk.Label(frame,text= "Last_First")
last_firstLabel.grid(column=3, row=10, sticky=W)
phoneLabel = ttk.Label(frame,text= "Phone")
phoneLabel.grid(column=3, row=11, sticky=W)
searchButton = ttk.Button(frame, text="Search")
searchButton.grid(column=1, row=12, sticky=(W, E))
root.mainloop()