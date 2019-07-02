from PIL import Image, ImageDraw, ImageFont
import pystray
import _thread
import time
import Battery_info

class Tray_display():
    
    icon = None
    battery_level = 0

    def __init__(self):
        self.icon = pystray.Icon('battery_level_show')
    
    def create_icon_by_text(self, text):
        width = 200
        height = 200
        color1 = 0x000000
        color2 = 0xFFFFFF
        image = Image.new('RGB', (width, height), color1)
        dc = ImageDraw.Draw(image)
        dc.text((0,0),text,font=ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',190),fill = color2)
        self.icon.icon = image

    def run(self):
        self.get_battery_level()
        self.icon.run()
    
    def get_battery_level(self):
        self.battery_level = Battery_info.get_battery_level()
        icon_text = str(self.battery_level)
        if(self.battery_level == 100):
            icon_text = "F"
        self.create_icon_by_text(icon_text)
    
    def get_battery_level_thread(self):
        while(True):
            self.get_battery_level()
            time.sleep(1)

    def run_thread(self):
        _thread.start_new_thread(self.run, ())
        _thread.start_new_thread(self.get_battery_level_thread, ())