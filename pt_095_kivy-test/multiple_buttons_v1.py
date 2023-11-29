import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# colors
#name	 = [R,G,B,alpha]
red		 = [1,0,0,1]
green	 = [0,1,0,1]
blue	 = [0,0,1,1]
purple	 = [1,0,1,1]
colors	 = [red, green, blue, purple]


class HBoxLayoutExample(App):
	def build(self):
		layout = BoxLayout(padding=10)

		for i in range(5):
			btn = Button(text=f"Button #{i+1}",
						  background_color = random.choice(colors)
			)

			layout.add_widget(btn)

		return layout

if __name__ == '__main__':
	app = HBoxLayoutExample()
	app.run()

