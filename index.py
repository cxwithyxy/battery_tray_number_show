import Tray_display
from multiprocessing import Pool, freeze_support
import sys

def exit_app():
    sys.exit(0)

tray_display = Tray_display.Tray_display()
tray_display.set_exit_callback(exit_app)

def tray_display_multiprocessing():
    tray_display.run()

if __name__ == "__main__":
    freeze_support()
    po = Pool(1)

    po.apply_async(tray_display_multiprocessing)

    input("battery_tray_number_show start \n")