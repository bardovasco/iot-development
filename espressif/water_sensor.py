# The MIT License (MIT)
#
# Copyright (c) 2021 Erick Israel Vazquez Neri
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import utime as time
from machine import ADC, Pin


class WaterSensor:
    def __init__(self,sensor_pin=0, pulse_pin=15):
        self.sensor_pin = ADC(sensor_pin)
        self.pulse_pin = Pin(pulse_pin, Pin.OUT)
        self.db = 300
        self.MAX_LVL = 500
        self.PULSE_ON = 1
        self.PULSE_OFF = 0

    def pulse(self):
        self.pulse_pin.value(self.PULSE_ON)
        raw = self.sensor_pin.read()
        time.sleep_ms(self.db) # debounce ms
        raw = self.sensor_pin.read()
        self.pulse_pin.value(self.PULSE_OFF)
        return raw

    def read_raw(self):
        return self.pulse()

    def read_level(self):
        raw = self.pulse()
        return (raw * 100) // self.MAX_LVL
