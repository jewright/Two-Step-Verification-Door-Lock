import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from led import green_led_on, green_led_off, red_led_off, red_led_on
from timer import countdown


def rfid():
    green_led_off()
    red_led_on()

    print("Place your card.\n")
    jordyn = 910519800973
    reader = SimpleMFRC522()
    try:
        # Read Card ID
        id, text = reader.read()

        # Print ID data
        print(id)
        print(text)

    finally:
        GPIO.cleanup()
    if (id == jordyn):
        print("Jordyn, Access Granted")

        red_led_off()
        green_led_on()


    else:
        print("Access Denied. Wait 3 seconds. ")

        red_led_on()
        countdown(3)
        rfid()


