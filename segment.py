#!/usr/bin/python
# pip3 install raspberrypi-tm1637 - pygpio install from apt or pip. run (sudo pigpiod to have it running in the bagground)

import pigpio
from tm1637 import TM1637
from datetime import datetime
import time

# Initialize the pigpio library
pi = pigpio.pi()

# Create a TM1637 object
tm = TM1637(clk=27, dio=18)

try:
    # Display the time
    while True:
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second
        tm.numbers(hour, minute, colon=False)
        time.sleep(0.5)
        tm.numbers(hour, minute, colon=True)
        time.sleep(0.5)

except KeyboardInterrupt:
    # Turn off the display and release the pigpio library resources
    tm.write([0, 0, 0, 0])
    print("\nTime has stopped.")
    pi.stop()
