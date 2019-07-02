from ctypes import *

class PowerClass(Structure):
    _fields_ = [('ACLineStatus', c_byte),
            ('BatteryFlag', c_byte),
            ('BatteryLifePercent', c_byte),
            ('Reserved1',c_byte),
            ('BatteryLifeTime',c_ulong),
            ('BatteryFullLifeTime',c_ulong)]

def get_battery_level():
    powerclass = PowerClass()
    result = windll.kernel32.GetSystemPowerStatus( byref(powerclass) )
    return powerclass.BatteryLifePercent
