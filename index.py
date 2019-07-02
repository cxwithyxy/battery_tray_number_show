from PIL import Image, ImageDraw, ImageFont
import pystray
import _thread
import time

icon = pystray.Icon('battery_level_show')


def create_icon_by_text(text):
    width = 200
    height = 200
    color1 = 0x000000
    color2 = 0xFFFFFF
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.text((0,0),text,font=ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',190),fill = color2)

    return image

icon.icon = create_icon_by_text("99")

def do():
    icon.run()


battery_level = 0

def get_battery_level():
    global battery_level
    while(True):
        icon.icon = create_icon_by_text(str(battery_level))
        time.sleep(1)
        battery_level += 1



_thread.start_new_thread(do,())
_thread.start_new_thread(get_battery_level,())

input("121212")