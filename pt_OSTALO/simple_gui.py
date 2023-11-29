#! /usr/bin/python

# simple_gui

from Tkinter import *

# Creating window:
root = Tk()

# Modify root window:
root.title("Simple GUI (root window)")
root.geometry("400x200")

app = Frame(root)

# Display app:
app.grid()


button1 = Button(app, text = "THis is BUTTON 1")
button1.grid()

button2 = Button(app)
button2.grid()

label = Label(app, text = "This is a LABEL")

# Display a Label:
label.grid()

# start event loop:
root.mainloop()
