# !/usr/bin/env python

# imports

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import cv2
from led import (green_led_on, green_led_off, red_led_off, red_led_on)

import numpy as np
import os

from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle

#def trigger():
#    tri = 22
#    GPIO.setmode(GPIO.BCM)
#    GPIO.setup(tri,GPIO.OUT)

def main():
    def countdown(time_sec):
        while time_sec:
            mins, secs = divmod(time_sec, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            print()
            time.sleep(1)
            time_sec -= 1
        print("restart")
        main()



    green_led_off()
    red_led_on()

    print("Place your card.\n")
    bryan = 910519800973
    jordyn = 631564833849
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

    # current name only triggers when a person is identified
    currentname = "unknown"
    # Determine faces from encodings.pickle which is our trained model
    encodingsP = "encodings.pickle"

    print("[INFO] loading encodings + face detector...")
    data = pickle.loads(open(encodingsP, "rb").read())

    # src = camera feed
    vs = cv2.VideoCapture(0)
    time.sleep(2.0)

    # start the FPS counter
    fps = FPS().start()

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

        # loop over the facial embeddings
        for encoding in encodings:
            # attempt to match each face
            matches = face_recognition.compare_faces(data["encodings"],
                                                     encoding)
            name = "Unknown"  # if face is not recognized, then print Unknown

            # check to see if we have found a match
            if True in matches:
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}

                for i in matchedIdxs:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1
                print(counts)
                name = max(counts, key=counts.get)

                # if select people are identified, grant access
                if currentname != name:
                    currentname = name
                    print(currentname)
                    if id == jordyn and currentname == 'Jordyn':
                        print("Access Granted, Jordyn")
                        vs.release()
                        # do a bit of cleanup
                        cv2.destroyAllWindows()
                        countdown(5)

                    if currentname == 'Enisha':
                        print("Access Granted, Enisha")
                        #red_led_off()
                        #green_led_on()
                        #GPIO.output(tri, GPIO.HIGH)
                    if currentname == 'Bryan':
                        print("Access Granted, Bryan")
                        #red_led_off()
                        #green_led_on()
                        #GPIO.output(tri, GPIO.HIGH)
                    if currentname == 'Jeremiah':
                        print("Access Granted, Jeremiah")
                        #red_led_off()
                        #green_led_on()
                        #GPIO.output(tri, GPIO.HIGH)
                    else:
                        print('denied')
                        #green_led_off()
                        #red_led_on()
                        countdown(2)


            # update the list of names
            names.append(name)

        key = cv2.waitKey(1) & 0xFF

        # quit when 'q' key is pressed
        if key == ord("q"):
            break

        # update the FPS counter
        fps.update()

    # stop the timer and display FPS information
    fps.stop()
    print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    # do a bit of cleanup
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

# # imports
# from rfid import rfid
# from recognition import rec
# from led import green_led_on, green_led_off, red_led_off, red_led_on

# def main():

#     rfid()
#     rec()

# if __name__ == '__main__':
#     while True:
#         main()
