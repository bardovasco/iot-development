"""
This module provides interface to
connect esp8266 device to Wi-fi

Before executing, fill out the
WifiConfig object.
"""
import network
import time

# Wifi config
# environment variables
# object.
class WifiConfig:
    SSID = ''
    PASSWORD = ''


class WifiService(WifiConfig):
    def __init__(self, ssid, password):
        # Config
        self.SSID = ssid
        self.PASSWORD = password
        # WLAN Config
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

    def connect(self):
        self.wlan.connect(self.SSID, self.PASSWORD)
        # Loop message while device
        # connects to wifi network.
        while not self.wlan.isconnected:
            print('Connecting to %s' % self.SSID)
            time.sleep(.5)
        # Successfull connection.
        print('Connected to %s' % self.SSID)
        print(self.wlan.ifconfig())

