# Builder ile görsel tasarım yükleme

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

# KV KivyMD uygulamalarının görsel tarafının iskeleti, widgetlar buraya yazılıyor.
# Buradaki gibi bir string ya da ayrı bir .kv dosyası olabilir.

KV = '''
MDScreen:
    radius: [50, 0, 50, 0]
    md_bg_color: app.theme_cls.primary_color

    MDRaisedButton:
        text: "primary_light"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        md_bg_color: app.theme_cls.primary_light
        elevation: 10

    MDRaisedButton:
        text: "primary_color"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10

    MDRaisedButton:
        text: "primary_dark"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        md_bg_color: app.theme_cls.primary_dark
        elevation: 10
        gsdgsgsdgsdg
    MDRaisedButton:
        text: "no elevation"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        md_bg_color: app.theme_cls.primary_dark
'''

Window.size = (360, 640)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"
        return Builder.load_string(KV)


MainApp().run()
