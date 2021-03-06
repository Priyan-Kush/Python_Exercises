from tkinter import *
from tkinter import ttk


root = Tk()
var1 = StringVar()
var2 = StringVar()
root.title("Employee")
root.geometry("400x400")
frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
flightNoLabel = ttk.Label(frame, text="Empid")
flightNoLabel.grid(column=0, row=0, sticky=W)
flightNo = ttk.Entry(frame)
flightNo.grid(column=1, row=0, sticky=(W, E))
nameLabel = ttk.Label(frame, text="Employee Name")
nameLabel.grid(column=0, row=1, sticky=W)
name = ttk.Entry(frame)
name.grid(column=1, row=1, sticky=(W, E))
flightLabel = ttk.Label(frame, text="Job")
flightLabel.grid(column=0, row=2, sticky=W)
flight = ttk.Entry(frame)
flight.grid(column=1, row=2, sticky=(W, E))
flight.insert(0,"Manager")
sourceLabel = ttk.Label(frame, text="Source")
sourceLabel.grid(column=0, row=3, sticky=W)
sourceRadioButton1 = ttk.Radiobutton(frame,text = "Regular",value=0,variable=var1)
sourceRadioButton1.grid(column=1, row=3, sticky=(W, E))
sourceRadioButton2 = ttk.Radiobutton(frame,text = "Temporary",value=1,variable=var1)
sourceRadioButton2.grid(column=2, row=3, sticky=(W, E))
destinationLabel = ttk.Label(frame, text="Employee Type")

durationLabel = ttk.Label(frame, text="Salary")
durationLabel.grid(column=0, row=5, sticky=W)
durationSpinbox = ttk.Spinbox(frame,from_=0,to=200)
durationSpinbox.grid(column=1, row=5, sticky=(W, E))
durationSpinbox.insert(0, "19")
insertButton = ttk.Button(frame, text="Insert")
insertButton.grid(column=0, row=6, sticky=(W, E))
updateButton = ttk.Button(frame, text="Update")
updateButton.grid(column=1, row=6, sticky=(W, E))
deleteButton = ttk.Button(frame, text="Delete")
deleteButton.grid(column=0, row=7, sticky=(W, E))
selectButton = ttk.Button(frame, text="Select")
selectButton.grid(column=1, row=7, sticky=(W, E))

root.mainloop()