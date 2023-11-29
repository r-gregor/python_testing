# from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

def myClick():
	myLabel1 = tk.Label(root, text="Hey! You just clicked Me!!")
	myLabel1.pack()


myButton1 = tk.Button(root, text="Click Me!", state=tk.DISABLED)
myButton1.pack()

myButton2 = tk.Button(root, text="Click Me!")
myButton2.pack()

myButton3 = tk.Button(root, text="Click Me!", padx=50, pady=20)
myButton3.pack()

myButton4 = tk.Button(root, text="Click Me! (with action)", padx=60, command=myClick, fg="light blue", bg="grey")
myButton4.pack()







root.mainloop()
