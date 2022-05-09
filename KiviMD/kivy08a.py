# BUTTON COUNTER EXAMPLE WITH SCREEN MANAGER CODED IN PY FILE


from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

# python main.py --size=360x640 --dpi=441
Window.size = (360, 640)
Window.dpi = 441

# global değişkenimiz counter
counter = 0

class MainApp(MDApp):

    def build(self):
        self.title = "My Material Application"
        self.theme_cls.primary_palette = "Blue"

        return Builder.load_file('kivy08a.kv')

    def increase_counter(self):
        global counter
        counter += 1
        print(counter)
        self.root.ids["counterLabel"].text = str(counter)

if __name__ == '__main__':
    MainApp().run()

