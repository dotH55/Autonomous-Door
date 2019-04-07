# Autonomous Door
# Author: Habilou Sanwidi
# This code incorporates two python classes from Github written by Daniel Agar"
# __init__.py & bt_rssi.py
# https://github.com/ewen/bluetooth-proximity.git"

import time
import sys
import os
import RPi.GPIO as GPIO
from bt_proximity import BluetoothRSSI

# Address of the key
BT_ADDR = 'B8:27:EB:FB:45:BC'

# This method is in charge of unlocking,
# opening, closing and locking the door
def execution():
    os.system("python3 UnlockDoor.py")
    time.sleep(3)
    os.system("python OpenDoor.py")
    time.sleep(8)
    os.system("python CloseDoor.py")
    time.sleep(5)
    os.system("python3 LockDoor.py")
    time.sleep(3)
        
def print_usage():
    print ("Usage: python AutoDoor.py [-e]")


def main():

    print("Autonomous Door starting...")
    # Always keep your door locked
    os.system("python3 LockDoor.py")
    addr = BT_ADDR
    # Arguments for specify actions
    if (len(sys.argv) > 1):
        if sys.argv[1] == "-e":
            execution()
            quit()
        elif sys.argv[1] == "-u":
            os.system("python3 UnlockDoor.py")
            quit()
        elif sys.argv[1] == "-l":
            os.system("python3 LockDoor.py")
            quit()
        elif sys.argv[1] == "-o":
            os.system("python3 UnlockDoor.py")
            time.sleep(3)
            os.system("python OpenDoor.py")
            quit()
        elif sys.argv[1] == "-c":
            os.system("python3 UnlockDoor.py")
            time.sleep(2)
            os.system("python CloseDoor.py")
            time.sleep(7)
            os.system("python3 LockDoor.py")
            quit()
        
        else:
            print(sys.argv[1])
            addr = sys.argv[1]
    
    btrssi = BluetoothRSSI(addr=addr)    
    while True:
        print btrssi.get_rssi()
        time.sleep(1)
        if (btrssi.get_rssi() == None):
            btrssi = BluetoothRSSI(BT_ADDR)
            print("Not in range")
            time.sleep(5)
        elif (btrssi.get_rssi() > -10):
            execution()
            time.sleep(5)
            print("Safe to proceed")
            
if __name__ == '__main__':
    main()
