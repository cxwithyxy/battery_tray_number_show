import Tray_display
from multiprocessing import Pool 

tray_display = Tray_display.Tray_display()

def tray_display_multiprocessing():
    tray_display.run()

if __name__ == "__main__":
    po = Pool(1)

    po.apply_async(tray_display_multiprocessing)

    input("121212")