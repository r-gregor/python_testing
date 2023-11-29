import tkinter as tk


def myClick():
	greet = "Hello, " + efield1.get() + "!"
	myLabel1 = tk.Label(root, text=greet)
	myLabel1.pack()

def submitMail():
	entry = efield2.get()
	if not "@" in entry:
		line = "Ooops. Not a valid email address. Try again."
	else:
		line = "Sending data to, " + entry + "!"

	myLabel2 = tk.Label(root, text=line)
	myLabel2.pack()


root = tk.Tk()
root.geometry("600x400")

efield1 = tk.Entry(root, width=40)
efield1.pack()

myButton1 = tk.Button(root, text="Enter your name", padx=60, command=myClick)
myButton1.pack()

efield2 = tk.Entry(root, width=40)
efield2.insert(0, "Enter your email")
efield2.pack()

myButton2 = tk.Button(root, text="submit", padx=60, command=submitMail)
myButton2.pack()







root.mainloop()
