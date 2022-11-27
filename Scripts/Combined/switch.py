# !/usr/bin/env python
import RPi.GPIO as GPIO
import time

#   SHED DOOR SENSOR
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(19, GPIO.RISING)
    print("door open")
    GPIO.output(26, GPIO.LOW)

    GPIO.wait_for_edge(19, GPIO.FALLING)

    print("door closed")
    GPIO.output(26, GPIO.HIGH)