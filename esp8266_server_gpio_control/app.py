"""
This application intends to control
two gpio to control movement of a RC
car through a webpage.

The webpage will be deployed locally,
so, to access it we will access the
IP address provided at boot.

picocom REPL command

    picocom -b 115200 -r -l /dev/ttyUSB0

"""
from services import WifiService, Server, DeviceControl
from public import template


# App config
class AppConfig:
    SSID = ''
    PASSWORD = ''

# Init wifi service
wlan = WifiService(AppConfig.SSID, AppConfig.PASSWORD)
wlan.connect() # connect to wifi

# Init server
server = Server(address='', port=80, limit=1)

# Device control service
control = DeviceControl()

# App main loop
def init_app():
    while True:
        # Enter server listener
        # and return request
        request = server.read()

        if request.find('/control=fwd') == 6:
            control.move_fwd()
        elif request.find('/control=bwd') == 6:
            control.move_bwd()

        # Respond with template
        webpage = template()
        server.send(webpage)

