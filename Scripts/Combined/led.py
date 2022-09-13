import RPi.GPIO as GPIO
import time


def green_led_on():
    LED_PIN_G = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN_G, GPIO.OUT)
    GPIO.output(LED_PIN_G, GPIO.HIGH)


def green_led_off():
    LED_PIN_G = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN_G, GPIO.OUT)
    GPIO.output(LED_PIN_G, GPIO.LOW)
    GPIO.cleanup()

def red_led_on():
    LED_PIN_R = 27
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN_R, GPIO.OUT)
    GPIO.output(LED_PIN_R, GPIO.HIGH)


def red_led_off():
    LED_PIN_R = 27
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN_R, GPIO.OUT)
    GPIO.output(LED_PIN_R, GPIO.LOW)
    GPIO.cleanup()
