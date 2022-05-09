from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.toast import toast
from kivy.lang import Builder

Window.size = (360, 640)

KV = '''
MDScreen:
    
    MDTextField:
        id: inputText
        hint_text: "Lütfen şifreyi giriniz..."
        helper_text_mode: "on_focus"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        icon_right: "key"
        size_hint_x: None
        width: 250
        password: True

    MDRectangleFlatButton:
        text: "Hello, World"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_press: app.onClick()
'''
# KV içinde event'lara erişirken MDApp içindeyse app. ile, 
# başka bir class içindeyse root. ile ulaşabiliriz.

class MainApp(MDApp):
        
    def build(self):
        self.theme_cls.primary_palette = "Purple"  # "Green", "Red"
        self.theme_cls.primary_hue = "500"  # "200"
        self.root = Builder.load_string(KV)
        

    def onClick(self):
        # self.root'a KV stringini atadığımız için self.root.ids ile çağırıyoruz
        password = self.root.ids["inputText"].text
        if len(password) > 0:
            print(password)
        else:
            toast('Lütfen şifreyi giriniz...')
        # print(password if len(password) > 0 else toast('Lütfen şifreyi giriniz...'))

MainApp().run()
