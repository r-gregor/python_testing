from tkinter import *
from tkinter import filedialog

win = Tk() # 1 Create instance
win.title("Multitas") # 2 Add a title
win.resizable(0, 0) # 3 Disable resizing the GUI

# 4 Create a label
aLabel = Label(win, text="Remove duplicate file")
aLabel.grid(column=0, row=0) # 5 Position the label

# 6 Create a selectFile function to be used by button
def selectFile():

	filename = filedialog.askopenfilename(initialdir="/", title="Select file")
	print(filename) # 7 print the filename from the selected file

# 8 Adding a Button
action = Button(win, text="Search File", command=selectFile)
action.grid(column=0, row=1) # 9 Position the button

win.mainloop()  # 10 start GUI
