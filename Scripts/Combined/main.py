# !/usr/bin/env python

# imports

import pickle
import time
import RPi.GPIO as GPIO
import cv2
import face_recognition
from led import (green_led_on, green_led_off, red_led_off, red_led_on,blue_led_off,blue_led_on)
from mfrc522 import SimpleMFRC522


def main():
    def granted(time_sec):
        print("Access Granted")
        red_led_off()
        green_led_on()

        triggerPIN = 20
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(triggerPIN, GPIO.OUT)
        GPIO.output(triggerPIN, GPIO.HIGH)

        while time_sec:
            mins, secs = divmod(time_sec, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            print()
            time.sleep(1)
            time_sec -= 1
        print("restart")
        GPIO.output(triggerPIN, GPIO.LOW)
        green_led_off()
        main()

    def denied(time_sec):
        print("Access Denied")
        red_led_off()
        green_led_off()
        time.sleep(1)
        red_led_on()
        time.sleep(1)
        red_led_off()
        time.sleep(1)
        red_led_on()
        time.sleep(1)

        # while time_sec:
        #     mins, secs = divmod(time_sec, 60)
        #     timeformat = '{:02d}:{:02d}'.format(mins, secs)
        #     print(timeformat, end='\r')
        #     print()
        #     red_led_off()
        #     time.sleep(1)
        #     red_led_on()
        #     time_sec -= 1
        print("restart")
        main()

    # LEDs
    red_led_on()

    # RFID Input
    print("Place your card.\n")
    # Card Assignments
    master = 81927640272
    bryan = 771953824915
    jordyn = 360041780282
    jeremiah = 222217475115
    enisha = 976973435944

    reader = SimpleMFRC522()
    try:
        # Read Card ID
        id, text = reader.read()
        # Print ID data
        print(id)
        print(text)
    finally:
        GPIO.cleanup()

    if id == jordyn:
        print("Jordyn, Access Granted")
        pass
    elif id == enisha:
        print("Enisha, Access Granted")
        pass
    elif id == bryan:
        print("Bryan, Access Granted")
        pass
    elif id == jeremiah:
        print("Jeremiah, Access Granted")
        pass
    elif id == master:
        granted(5)
    else:
        print("Access Denied. Wait 3 seconds. ")
        denied(3)

    # green_led_on()
    # red_led_off()

    currentname = "unknown"
    encodingsP = "encodings.pickle"

    print("[INFO] loading encodings + face detector...")

    data = pickle.loads(open(encodingsP, "rb").read())

    # Set frame size to speed up camera loading
    vs = cv2.VideoCapture(0)
    vs.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    vs.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    blue_led_on()
    while True:
        ret, frame = vs.read()
        boxes = face_recognition.face_locations(frame)
        encodings = face_recognition.face_encodings(frame, boxes)
        names = []
        # cv2.imshow('',frame)

        for encoding in encodings:
            matches = face_recognition.compare_faces(data["encodings"], encoding)
            name = "Unknown"

            if True in matches:
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}

                for i in matchedIdxs:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1
                print(counts)
                name = max(counts, key=counts.get)

                if currentname != name:
                    currentname = name
                    print(currentname)
                    if id == jordyn and currentname == 'Jordyn':
                        print("Access Granted, Jordyn")
                        pass
                    elif id == enisha and currentname == 'Enisha':
                        print("Access Granted, Enisha")
                        pass
                    elif id == bryan and currentname == 'Bryan':
                        print("Access Granted, Bryan")
                        pass
                    elif id == jeremiah and currentname == 'Jeremiah':
                        print("Access Granted, Jeremiah")
                        pass
                    else:
                        vs.release()
                        cv2.destroyAllWindows()
                        denied(3)
                    blue_led_off()
                    vs.release()
                    cv2.destroyAllWindows()
                    granted(5)

            names.append(name)
        key = cv2.waitKey(1) & 0xFF
        # quit 'q' is pressed
        if key == ord("q"):
            break

    cv2.destroyAllWindows()
    vs.stop()


if __name__ == '__main__':
    while True:
        main()
