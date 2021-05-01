"""
Module focused on controlling
gpios.
"""
from machine import Pin


class GPIO:
    gpio_output_fwd = Pin(4, Pin.OUT)
    gpio_output_bwd = Pin(5, Pin.OUT)


class DeviceControl(GPIO):
    def __init__(self):
        self.gpio_output_fwd.value(0)
        self.gpio_output_bwd.value(0)

    def move_fwd(self):
        self.gpio_output_fwd.value(1)
        self.gpio_output_bwd.value(0)

    def move_bwd(self):
        self.gpio_output_fwd.value(0)
        self.gpio_output_bwd.value(1)

