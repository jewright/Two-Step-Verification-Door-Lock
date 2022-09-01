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
