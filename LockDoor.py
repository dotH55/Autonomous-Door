"""This program locks the door by positioning 
the servo at 50 degree."""

import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 16 for Shield/HAT/Bonnet.

kit = ServoKit(channels=16)
kit.servo[0].angle = 50
