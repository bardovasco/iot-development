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
"""
@@@ Micropython & ESP32/ESP8266 PushButton @@@

This module grants the flexibility to customize
the supported button values by the implementation
(i.e. simple, double, triple, etc) by taking
receiving callbacks for short and long presses
accordingly.
Once their respective timeouts have expired, the
callback will be executed receiving the following
keyword arguments:

    sp_cb(p_count: int, tick: int) # short press callback
    lp_cb(tick: int)               # long press callback

Additionally, as this class works as a coroutine,
once the PushButton object gets instantiated, a new
task/coro will be created as well.
"""
import uasyncio as asyncio
import utime as time


class PushButton:
    def __init__(self, pin, sp_cb=None, lp_cb=None, sp_to=800, lp_to=2000):
        self.pin = pin
        self.sp_cb = sp_cb              # Short press callback
        self.lp_cb = lp_cb              # Long press callback
        self.sp_to = sp_to              # Short press timeout
        self.lp_to = lp_to              # Long press timeout
        self.debounce = 300             # ms
        self.sense = self.pin.value()   # Def logical state
        self.state = self.rawstate()    # Initial state
        # Create task
        asyncio.create_task(self.get_button_event())

    def rawstate(self):
        return bool(self.pin.value() ^ self.sense)

    async def get_button_event(self):
        t_out = None # Timeout handler
        p_count = 0

        while True:
            last_state = self.rawstate()

            if last_state != self.state:
                await asyncio.sleep_ms(self.debounce)
                self.state = last_state
                if self.state == 1:
                    t_out = time.ticks_ms()  # init timeout
                    p_count += 1
            elif p_count > 0:
                if self.state != 1 and time.ticks_diff(time.ticks_ms(), t_out) > self.sp_to:
                    if self.sp_cb:
                        self.sp_cb(p_count=p_count, tick=time.ticks_ms()) # call short press callback
                    else:
                        print('sp_cb, p_count: %i, tick: %i' % (p_count, time.ticks_ms()))
                    p_count = 0
                elif self.state == 1 and time.ticks_diff(time.ticks_ms(), t_out) > self.lp_to:
                    if self.lp_cb:
                        self.lp_cb(tick=time.ticks_ms()) # call long press callback
                    else:
                        print('lp_cb, p_count: %i, tick: %i' % (p_count, time.ticks_ms()))
                    p_count = 0
