import ubinascii
from network import Bluetooth

import time

# 

while True:
    print("")
    time.sleep(30)

"""
bluetooth = Bluetooth()
bluetooth_devices = []

bluetooth.start_scan(5)
while bluetooth.isscanning():
    adv = bluetooth.get_adv()
    if adv:
        # try to get the complete name
        #print(bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL))

        mfg_data = bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_MANUFACTURER_DATA)
        if mfg_data:
            # try to get the manufacturer data (Apple's iBeacon data is sent here)
            # print(ubinascii.hexlify(mfg_data))
            bDev = ubinascii.hexlify(mfg_data)
            if bDev not in bluetooth_devices:
                bluetooth_devices.append(bDev)


print(bluetooth_devices)"""

"""
from machine import RTC
from network import WLAN
import machine

# Conectar a mi wifi
wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid='vodafoneAA35ED', auth=(WLAN.WPA2, 'Pk9JyhkYeXypaer9'))
while not wlan.isconnected():
    machine.idle()
print("WiFi connected succesfully")

# RTC
rtc = RTC()
rtc.ntp_sync("es.pool.ntp.org")
print(rtc.now())
"""