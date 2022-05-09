from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton


"""
primary_palette:
The name of the color scheme that the application will use. All major 
material components will have the color of the 
specified color theme.

Available options are: ‘Red’, ‘Pink’, ‘Purple’, ‘DeepPurple’, ‘Indigo’, 
‘Blue’, ‘LightBlue’, ‘Cyan’, ‘Teal’, ‘Green’, 
‘LightGreen’, ‘Lime’, ‘Yellow’, ‘Amber’, ‘Orange’, ‘DeepOrange’, ‘Brown’, 
‘Gray’, ‘BlueGray’.

primary_hue:

The color hue of the application.
Available options are: ‘50’, ‘100’, ‘200’, ‘300’, ‘400’, ‘500’, ‘600’, ‘700’, 
‘800’, ‘900’, ‘A100’, ‘A200’, ‘A400’, ‘A700’.

"""

Window.size = (360, 640)

class MainApp(MDApp):
        
    def build(self):
        self.theme_cls.primary_palette = "Purple"  # "Green", "Red"
        self.theme_cls.primary_hue = "500"  # "200"
        screen = MDScreen()
        screen.add_widget(
            MDRectangleFlatButton(
                text = "Hello, World",
                pos_hint = {"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen


MainApp().run()
