#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

Jordyn = 84863325306


try:
        id, text = reader.read()
        if (id == Jordyn):
                print("Jordyn: Access Authorized")
        else:
                print("Access Denied")
finally:
        GPIO.cleanup()

""" 
SDA = Pin 24
SCK = Pin 23
MOSI = Pin 19
MISO = Pin 21
GND = Pin 6
RST = Pin 22
3.3V = Pin 1
"""