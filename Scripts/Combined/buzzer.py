
import RPi.GPIO as GPIO
import time

def Buzzer():
    triggerPIN = 20
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(triggerPIN, GPIO.OUT)
    GPIO.output(triggerPIN, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(triggerPIN, GPIO.LOW)




