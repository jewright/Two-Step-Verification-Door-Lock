#!/usr/bin/env python

# imports : Raspberry Pi GIPO interface & RFID library 
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
try:
        # Read Card ID
        id, text = reader.read()
        
        # Print ID data
        print(id)
        print(text)
finally:
        GPIO.cleanup()
