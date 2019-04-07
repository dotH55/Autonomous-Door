#This program closes the door

import time
import RPi.GPIO as GPIO

def main():

    print("Close Door")
    # Pin setup
    doorC = 17
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(doorC, GPIO.OUT)
    time.sleep(1)
    # This loop makes the motor turn a bit slower
    for i in range(0, 800):
        GPIO.output(doorC, True)
        time.sleep(.001)
        GPIO.output(doorC, False)

    # Free pins
    GPIO.cleanup()

if __name__ == '__main__':
    main()
