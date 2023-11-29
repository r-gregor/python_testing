# must be run from py command (win10 version of python 3.9) so that gui can work

import os
import tkinter as tk

os.system('clear')

root = tk.Tk()
root.title('Greg gui - try 1')
# root.geometry('400x400')

def hello():
	hello_label = tk.Label(root, text="Hello " + myTextBox1.get())
	hello_label.grid()

myLabel1 = tk.Label(root, text="Enter your first name:").grid(row=0, column=0)
# myLabel1.grid(row=0, column=0)

myTextBox1 = tk.Entry(root, width=30)
myTextBox1.grid(row=0, column=1)

myButton1 = tk.Button(root, text="Submit", command=hello).grid(row=1, column=1)
# myButton1.grid(row=1, column=1)

root.mainloop()