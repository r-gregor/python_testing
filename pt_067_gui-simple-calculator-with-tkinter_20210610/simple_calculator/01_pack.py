# must be run from py command (win10 version of python 3.9) so that gui can work

import os
import tkinter as tk

os.system('clear')

root = tk.Tk()
root.title('Greg gui - try 1')
root.geometry('400x400')

def hello():
	hello = tk.Label(root, text="Hello " + myTextBox1.get())
	hello.pack()

myLabel1 = tk.Label(root, text="Enter your first name:")
myLabel1.pack()

myTextBox1 = tk.Entry(root, width=30)
myTextBox1.pack()

myButton1 = tk.Button(root, text="Submit", command=hello)
myButton1.pack()

root.mainloop()