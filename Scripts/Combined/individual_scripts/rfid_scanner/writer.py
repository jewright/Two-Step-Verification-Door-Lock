#!/usr/bin/env python

# imports : Raspberry Pi GIPO interface & RFID library 
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
try:
        # Assign ID to Card
        text = input('New data:')
        
        # Place Card to assign the ID to data
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
        
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