from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton

# python kivy02.py --size=360x640 --dpi=441
Window.size = (360, 640)
Window.dpi = 441

class MainApp(MDApp):
    def build(self):
        screen = MDScreen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen

MainApp().run()
