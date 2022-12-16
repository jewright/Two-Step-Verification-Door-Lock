import RPi.GPIO as GPIO

def green_led_on():
    ledG = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledG, GPIO.OUT)
    GPIO.output(ledG, GPIO.HIGH)

def green_led_off():
    ledG = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledG, GPIO.OUT)
    GPIO.output(ledG, GPIO.LOW)

def red_led_on():
    ledR = 27
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledR, GPIO.OUT)
    GPIO.output(ledR, GPIO.HIGH)

def red_led_off():
    ledR = 27
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledR, GPIO.OUT)
    GPIO.output(ledR, GPIO.LOW)

def blue_led_on():
    ledB = 26
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledB, GPIO.OUT)
    GPIO.output(ledB, GPIO.HIGH)

def blue_led_off():
    ledB = 26
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledB, GPIO.OUT)
    GPIO.output(ledB, GPIO.LOW)

# Green
# GPIO 17

# Red
# GPIO 27

