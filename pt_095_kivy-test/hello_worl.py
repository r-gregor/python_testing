# hello_world.py
# from: https://www.youtube.com/watch?v=crpQUc81THU
#       Starting With Kivy to Build Cross-Platform GUI Apps
#

from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        # v1 label = Label(text='Hello from Kivy')
        label = Label(text='Hello from Kivy',
                      font_size='40sp')

        return label

if __name__ == '__main__':
    app = MainApp()
    app.run()

