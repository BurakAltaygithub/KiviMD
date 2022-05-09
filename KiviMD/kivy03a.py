# Basit ekran ve buton ile buton eventi ekleme

from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton

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
                on_press = self.tiklama,
                line_color=(1,0,0,1)
            )
        )
        return screen

    def tiklama(self, btn):
        print("butona basıldı!!!")
        #print(btn)
        print("basılan button metni: ", btn.text)
        #print("basılan button pozisyonu: ", btn.pos_hint['center_x'])



MainApp().run()
