from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.toast import toast

Window.size = (360, 640)

class MainApp(MDApp):
        
    def build(self):
        self.theme_cls.primary_palette = "Purple"  # "Green", "Red"
        self.theme_cls.primary_hue = "500"  # "200"
        screen = MDScreen()
        # MDTextField text değerine ulaşabilek için bir yöntem
        self.inputText = MDTextField(
            # kv içerisinde id verilebiliyor ve self.root.ids["inputText"].text ile ulaşılabiliyor
            # id = "inputText", burada id veremiyoruz maalesef.
            hint_text = "Lütfen şifreyi giriniz...",
            helper_text_mode = "on_focus",
            pos_hint = {"center_x": 0.5, "center_y": 0.6},
            icon_right = "key",
            size_hint_x = None,
            width = 250,
            password = True,
        )
        screen.add_widget(self.inputText)
        
        screen.add_widget(
            MDRectangleFlatButton(
                text = "Hello, World",
                pos_hint = {"center_x": 0.5, "center_y": 0.5},
                on_press = self.onClick
            )
        )
        return screen

    def onClick(self, obj):
        password = self.inputText.text
        if len(password) > 0:
            print(password)
        else:
            toast('Lütfen şifreyi giriniz...')
        # print(password if len(password) > 0 else toast('Lütfen şifreyi giriniz...'))

MainApp().run()

