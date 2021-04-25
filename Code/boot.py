#
from network import Bluetooth, WLAN
#
import classes
import global_values


# Empezamos actualizando el RTC


# Inicializamos objetos
global_values.bluetooth = Bluetooth()
global_values.wlan = WLAN(mode=WLAN.STA)
# Inicializamos alarmas
global_values.alarmas = classes.Clock()