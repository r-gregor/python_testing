# img_viewer.py

from genericpath import isfile
import PySimpleGUI as sg
import os.path

# window layout of two columns
file_list_column = [
	[
		sg.Text("Image Folder"),
		sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
		sg.FolderBrowse(),
	],
	[
		sg.Listbox(
			values=[], enable_events=True, size=(40,20),
			key="-FILE LIST-"
		)
	
	],

]

image_viewer_column = [
	[sg.Text("Choose an image from the list on the left:")],
	[sg.Text(size=(40,10), key="-TOUT-")],
	[sg.Image(key="-IMAGE-")],
]



# ------------- full layout -----------------
layout = [
	[
		sg.Column(file_list_column),
		sg.VSeparator(),
		sg.Column(image_viewer_column),
	]
]

window = sg.Window("Image Viewer", layout)

# event loop
while True:
	event, values = window.read()

	# End program if user closes the Window or
	# presses the "OK" button.
	if event == "Exit" or event == sg.WIN_CLOSED:
		break

	if event == "-FOLDER-":
		folder = values["-FOLDER-"]
		try:
			file_list = os.listdir(folder)
		except:
			file_list = []

		fnames = [
			f
			for f in file_list
			if os.path.isfile(os.path.join(folder, f))

			# without pillov installed only *.png and *.gif files can be read!
			and f.lower().endswith((".png", ".gif"))
		]
		window["-FILE LIST-"].update(fnames)

	# a file was chosen from the files list!
	elif event == "-FILE LIST-":
		try:
			filename = os.path.join(
				values["-FOLDER-"], values["-FILE LIST-"][0]
			)
			window["-TOUT-"].update(filename)
			window["-IMAGE-"].update(filename=filename)
		except:
			pass

	
window.close()