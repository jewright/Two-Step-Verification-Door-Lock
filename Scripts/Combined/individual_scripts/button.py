from gpiozero import Button
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

count = 0
button = Button(16)

while True:
    button.wait_for_press()
    jordyn = 81927640272
    count = +1
    if count == 2:

            print("Place your card.\n")
            reader = SimpleMFRC522()
            # Read Card ID
            id, text = reader.read()
            # Print ID data
            print(id)
            print(text)
            if id == jordyn:
                print("Jordyn, Access Granted")
    print('Button Pressed...', count)

