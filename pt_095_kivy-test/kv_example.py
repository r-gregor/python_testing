# kv_example.py
# example of using kv language:
# - Separate Interface design from Application Logic
# - Follows Separation of Conserns Prnciple
# - Part of Model-View-Controller Architectural Pattern

# program will look for button.kv !!
from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        return Button()

    def on_press_button(self):
        print('You pressed the button!')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()

