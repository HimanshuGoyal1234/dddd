# from importlib import reload
# import random
# import time
# import psutil
# from CWH import alpha
# def battery_alert():
#     while True:
#         time.sleep(10)
#         battery = psutil.sensors_battery()
#         percent = int(battery.percent)
#         if percent < 30:
#             import Dialogs.Dialog as full_battery
#             reload(full_battery)
#             alpha(f"{random.choice(full_battery.low_b())}")
#         elif percent < 10:
#             import Dialogs.Dialog as full_battery

#             reload(full_battery)
#             alpha(f"{random.choice(full_battery.last_low())}")
#         elif percent == 100:
#             import Dialogs.Dialog as full_battery

#             reload(full_battery)
#             alpha(f"{random.choice(full_battery.full_battery())}")
#         else:
#             pass

# def check_plugin_status():
#     battery = psutil.sensors_battery()
#     previous_state = battery.power_plugged

#     while True:
#         battery = psutil.sensors_battery()

#         if battery.power_plugged != previous_state:
#             if battery.power_plugged:
#                 import Dialogs.Dialog as full_battery
#                 reload(full_battery)
#                 alpha(f"{random.choice(full_battery.plug_in)}")
#             else:
#                 import Dialogs.Dialog as full_battery
#                 reload(full_battery)
#                 alpha(f"{random.choice(full_battery.plug_out)}")
#             previous_state = battery.power_plugged
# check_plugin_status()
# def battey_persentage():
#     battery = psutil.sensors_battery()
#     percent = int(battery.percent)
#     return percent

# # battery_alert()
# # check_plugin_status()


import random
import psutil


from importlib import reload

from all_important_functions import _drive_selection_
from all_important_functions import alpha
battery = psutil.sensors_battery()
_battery =  battery.percent
plugh = battery.power_plugged
def main():
    if plugh==False:
        if _battery < 10:
            import Dialogs.Dialog as full_battery
            reload(full_battery)
            alpha(f"{random.choice(full_battery.last_low)}")
        elif _battery>50:
            import Dialogs.Dialog as full_battery
            reload(full_battery)
            alpha(f"{random.choice(full_battery._greater_than_50)}")
    elif plugh==True:
        if _battery < 30:
            import Dialogs.Dialog as full_battery
            reload(full_battery)
            alpha(f"{random.choice(full_battery.low_b)}")
        elif _battery < 10:
            import Dialogs.Dialog as full_battery
            reload(full_battery)
            alpha(f"{random.choice(full_battery.last_low)}")
        elif _battery>50:
            import Dialogs.Dialog as full_battery
            reload(full_battery)
            alpha(f"{random.choice(full_battery._greater_than_50)}")

        elif _battery == 100:
            import Dialogs.Dialog as full_battery
            reload(full_battery)
            alpha(f"{random.choice(full_battery.full_battery)}")
        else:
            pass