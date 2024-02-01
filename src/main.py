import pyb
import time
from motor_driver import MotorDriver

pinA10 = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
pinB4 = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP) 
pinB5 = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP) 

# pinA10.high() # Set pin A10 to high enabling the motor

tim3 = pyb.Timer(3, freq=20000)

motor = MotorDriver(pinA10, pinB4, pinB5, tim3)

# ch1 = tim3.channel(1, pyb.Timer.PWM, pin=pinB4)
# ch2 = tim3.channel(2, pyb.Timer.PWM, pin=pinB5)
# 
# Moving one direction
# ch1.pulse_width_percent(0)
# ch2.pulse_width_percent(50)
motor.set_duty_cycle(50)

time.sleep(2)

# Moving in the OTHERx direction
# ch2.pulse_width_percent(0)
# ch1.pulse_width_percent(50)
motor.set_duty_cycle(-50)

time.sleep(2)

motor.set_duty_cycle(0)