#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

Jordyn = 360041780282
Bryan = 16629404792

try:
        id, text = reader.read()
        if (id == Jordyn):
                print("Jordyn: Access Authorized")
        if(id == Bryan):
                print("Bryan: Access Denied")
finally:
        GPIO.cleanup()