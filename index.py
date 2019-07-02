import pystray

icon = pystray.Icon('test name')

from PIL import Image, ImageDraw

def create_image():
    # Generate an image and draw a pattern
    width = 20
    height = 20
    color1 = 0x000000
    color2 = 0xFFFFFF
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image

icon.icon = create_image()

icon.run()