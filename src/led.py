import pyb
import time

pinA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP) # Initialize A0 as output
tim2 = pyb.Timer(2, freq=20000)
ch2 = tim2.channel(1, pyb.Timer.PWM_INVERTED, pin=pinA0)
ch2.pulse_width_percent(100)

while True:
    pass