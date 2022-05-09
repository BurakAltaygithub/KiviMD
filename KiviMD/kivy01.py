from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton

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


#class myApp(MDApp):
  #  def build(self):
 #       ekran = MDScreen()
  #      button = MDRectangleFlatButton(text="Merhaba Dünya!!", 
  #                                     pos_hint={"center_x": 0.5, "center_y": 0.8})
   #     
   #     button1 = MDRectangleFlatButton(text="Merhaba Ay!!", 
     #                                  pos_hint={"center_x": 0.3, "center_y": 0.5})
        
    #    button.text = "değiştirildi"
        
        
     #   ekran.add_widget(button)
     #   ekran.add_widget(button1)
      #  return ekran

#myApp().run()


