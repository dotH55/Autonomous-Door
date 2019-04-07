#This program opens the door

import time
import RPi.GPIO as GPIO

def main():

    print("Open Door")
    # Pin setup
    doorO = 4
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(doorO, GPIO.OUT)
    time.sleep(1)
    # This loop makes the motor turn a bit slower
    for i in range(0, 800):
        GPIO.output(doorO, True)
        time.sleep(.001)
        GPIO.output(doorO, False)

    # Free pins
    GPIO.cleanup()

if __name__ == '__main__':
    main()
