
import requests

from logging import root

from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.properties import StringProperty, NumericProperty

from kivymd.toast import toast
from kivy.uix.scrollview import ScrollView

from kivy.core.window import Window
Window.size = (400, 750) # in win mode
# Window.fullscreen = "auto"


# ++++++++++++++++++++++++ SCREEN MANAGER +++++++++++++++++++++++++

class MainPage(ScreenManager): 
    # height = NumericProperty()
    # weight = NumericProperty()
    bmi_calc = "No data requested yet."
    bmi_result = StringProperty(bmi_calc)
    
    

# ++++++++++++++++++++++++ FUNCTIONS 0f SCREEN MEASURE +++++++++++++++++++++++++
    def check_input(self):
        height_input = self.ids.height.text
        weight_input = self.ids.weight.text
                
        
        if ( len(height_input) > 0 and  len(height_input) <= 2) and (len(weight_input) > 1 and len(weight_input) <= 3):
                        
            # toast("Data entries okay !")

            payload = {"height": height_input, "weight" : weight_input}
            
            try:
                r = requests.get('http://127.0.0.1:8000/bmicalc', params = payload) # do request to backend
                r.raise_for_status()   
                
                r_dict = r.json()
                print("Backend contacted")

                bmi_calc = r_dict["data"] 
                self.ids.bmi_result.text = bmi_calc

            except requests.exceptions.HTTPError as errh:
                toast("HTTP Error "+repr(errh)) 
            except requests.exceptions.ConnectionError as errc:
                toast("Connection to API Error "+repr(errc))
            except requests.exceptions.Timeout as errt:
                toast("Timeout Error "+repr(errt))
            except requests.exceptions.RequestException as err:
                toast("Unknown Error "+repr(err))
            
            
                        
        else:
            toast("Please correct input values !")


            
        
# ++++++++++++++++++++++++ MAIN APP +++++++++++++++++++++++++

class bmibackendApp(MDApp): 
    
    
    def on_start(self):
        #https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"

        
     
    def build(self):
        return MainPage() # read in the kv-file and build the screen

    

if __name__ == '__main__':
    app = bmibackendApp()
    app.run()