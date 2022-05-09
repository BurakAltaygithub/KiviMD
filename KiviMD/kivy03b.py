# Basit ekran ve buton ile buton eventi ekleme (KV görsel tanımlama)

from kivymd.app import MDApp
from kivy.core.window import Window
# from kivymd.uix.screen import MDScreen
# from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder

Window.size = (360, 640)

# kv_str = '''
# MDScreen:
#     MDRectangleFlatButton:
#         text: "Topla (kv stringinden geldi)"
#         pos_hint: {"center_x": 0.5, "center_y": 0.5}
#         on_press: app.topla(2, 12)
# '''

class MainApp(MDApp):
        
    def build(self):
        self.theme_cls.primary_palette = "Purple"  # "Green", "Red"
        self.theme_cls.primary_hue = "500"  # "200"
        #self.root =  Builder.load_string(kv_str)
        self.root =  Builder.load_file("kivy03b.kv")
        #return Builder.load_string(uix)

    # eventi çağıran nesne ile ilgili bilgiler gerekmiyorsa burdaki btn parametresine gerek yok
    # btn parametresini kaldırınca kv stringinde on_press tanımlayabliyoruz.
    def tiklama(self, btn):
        print("butona basıldı!!!")
        #print(btn)
        print("basılan button metni: ", btn.text)
        #print("basılan button pozisyonu: ", btn.pos_hint['center_x'])
    
    def topla(self, a, b):
        c = a + b
        print(f"{a} ile {b} toplamı= ", c)
        #print("deneme çalıştı")



MainApp().run()
