# !/usr/bin/env python

# imports

import pickle
import time

import RPi.GPIO as GPIO
import cv2
import face_recognition
from led import (green_led_on, green_led_off, red_led_off, red_led_on)
from mfrc522 import SimpleMFRC522


def main():
    def countdown(time_sec):
        vs.release()
        cv2.destroyAllWindows()
        red_led_off
        green_led_on
        while time_sec:
            mins, secs = divmod(time_sec, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            print()
            time.sleep(1)
            time_sec -= 1
        print("restart")
        GPIO.cleanup()
        main()

    green_led_off()
    red_led_on()

    print("Place your card.\n")

    bryan = 771953824915
    jordyn = 360041780282
    jeremiah = 84863325306
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
        green_led_on()
        pass
    elif id == enisha:
        print("Enisha, Access Granted")
        green_led_on()
        pass
    elif id == bryan:
        print("Bryan, Access Granted")
        green_led_on()
        pass
    elif id == jeremiah:
        print("Jeremiah, Access Granted")
        green_led_on()
        pass
    else:
        print("Access Denied. Wait 3 seconds. ")
        countdown(3)

    green_led_off()
    red_led_on()

    currentname = "unknown"
    encodingsP = "encodings.pickle"

    print("[INFO] loading encodings + face detector...")

    data = pickle.loads(open(encodingsP, "rb").read())

    vs = cv2.VideoCapture(0)
    vs.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    vs.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # start the FPS counter
    # fps = FPS().start()

    # loop over frames from the video file stream
    while True:
        # grab the frame from the threaded video stream and resize it
        # to 500px (to speedup processing)
        ret, frame = vs.read()
        # Detect the face boxes
        boxes = face_recognition.face_locations(frame)
        # compute the facial embeddings for each face bounding box
        encodings = face_recognition.face_encodings(frame, boxes)
        names = []
        # cv2.imshow('',frame)

        for encoding in encodings:
            matches = face_recognition.compare_faces(data["encodings"],
                                                     encoding)
            # if face is not recognized, then print Unknown
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
                        countdown(5)
                    if id == enisha and currentname == 'Enisha':
                        print("Access Granted, Enisha")

                        countdown(5)
                    if id == bryan and currentname == 'Bryan':
                        print("Access Granted, Bryan")
                        countdown(5)
                    if id == jeremiah and currentname == 'Jeremiah':
                        print("Access Granted, Jeremiah")

                        countdown(5)
                    else:
                        print('Denied Access')
                        vs.release()
                        cv2.destroyAllWindows()
                        countdown(3)

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

""" 
SDA = Pin 24
SCK = Pin 23
MOSI = Pin 19
MISO = Pin 21
GND = Pin 6
RST = Pin 22
3.3V = Pin 1
"""
