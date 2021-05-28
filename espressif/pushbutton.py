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

# @@@ Micropython & ESP32/ESP8266 PushButton @@@
#
# This module grants the flexibility to customize
# the supported button values by the implementation
# (i.e. simple, double, triple, etc) by taking
# receiving callbacks for short and long presses
# accordingly.
# Once their respective timeouts have expired, the
# callback will be executed receiving the following
# keyword arguments:
#
#     self.cb(
#         evt:str,
#         cnt:int,
#         tick: int)
#
# Additionally, as this class works as a coroutine,
# once the PushButton object gets instantiated, a new
# task/coro will be created as well.
import uasyncio as asyncio
import utime as time


class PushButton:
    def __init__(self, pin, cb=None, spto=700, lpto=1500):
        self.pin = pin
        self.cb = cb                    # Callback
        self.spto = spto                # Short press timeout
        self.lpto = lpto                # Long press timeout
        self.db = 100                   # debounce ms
        self.sense = self.pin.value()   # Def logical state
        self.p = self.rawstate()        # pressed state
        # Create task
        asyncio.create_task(self.read_btn())

    def rawstate(self):
        return bool(self.pin.value() ^ self.sense)

    def is_tout(self, t_out, limit):
        t = time.ticks_diff(time.ticks_ms(), t_out)
        return t > limit

    async def read_btn(self):
        evt = None
        t_out = None
        cnt = 0

        while True:
            state = self.rawstate()

            if state != self.p:
                await asyncio.sleep_ms(self.db) # debounce press
                self.p = state
                if self.p:
                    # init timeout and
                    # press counts
                    t_out = time.ticks_ms()
                    cnt += 1
            elif cnt > 0:
                if not self.p and time.ticks_diff(time.ticks_ms(), t_out) > self.spto:
                    evt = 'short'
                    if self.cb:
                        self.cb(evt=evt, cnt=cnt, tick=time.ticks_ms())
                    else:
                        print('evt: %s, cnt: %i, tick: %i' % (evt, cnt, time.ticks_ms()))
                    cnt = 0
                elif self.p and time.ticks_diff(time.ticks_ms(), t_out) > self.lpto:
                    evt = 'long'
                    if self.cb:
                        self.cb(evt=evt, cnt=cnt, tick=time.ticks_ms())
                    else:
                        print('evt: %s, cnt: %i, tick: %i' % (evt, cnt, time.ticks_ms()))
                    cnt = 0

