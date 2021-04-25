# Importamos librerías micropython/Lopy
from machine import Timer
from network import Bluetooth, WLAN
import ubinascii
# Importamos nuestras propias funciones
import global_values


class Clock:

    def __init__(self):
        self.tiempoBluetooth = 60
        self.tiempoWifi = 60
        self.alarma_bluetooth = Timer.Alarm(self.ABluetooth, self.tiempoBluetooth, periodic=True)
        self.alarma_bluetooth = Timer.Alarm(self.AWifi, self.tiempoWifi, periodic=True)

    def ABluetooth(self, alarm):
        bluetoothScan()

    def AWifi(self, alarm):
        wifiScan()


def bluetoothScan():
    bluetooth_devices = []

    global_values.bluetooth.start_scan(5)
    while global_values.bluetooth.isscanning():
        adv = global_values.bluetooth.get_adv()
        if adv:
            if adv[0] not in bluetooth_devices:
                """
                0: mac, 1: addr_type, 2: adv_type
                3: rssi, 4: data
                """
                bluetooth_devices.append(adv[0])

    print('Hay %d dispositivos BLUETOOTH activos.' %(len(bluetooth_devices)))
    if len(bluetooth_devices) > 0:
        for dev in bluetooth_devices:
            print('\t',ubinascii.hexlify(dev),'    ', dev)


def wifiScan():
    myDevices = []
    wifi_devices = global_values.wlan.scan()
    print('Hay %d dispositivos WIFI activos.' %(len(wifi_devices)))
    for dev in wifi_devices:
        """
        0: ssid, 1: bssid, 2: sec,
        4: channel, 5: rssi
        """
        print('\t',dev[0])

        if dev[0] in global_values.my_wifi_devices:
            myDevices.append(dev[0])

    print('\n')
    if len(myDevices) > 0:
        for dev in myDevices:
            print('La red WIFI %s esta disponible!' %(dev))