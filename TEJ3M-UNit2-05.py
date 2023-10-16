# Copyright(c) 2023 Emmanuel Fofeyin All rights reserved.
# Created by : Emmanuel Fofeyin
# Created on : Oct 2023
# This Program make the servo spin but in python.

import time
import board
import pwmio
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.GP13, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
      
