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
    vs = VideoStream(src=0, framerate=10).start()
    time.sleep(2.0)

    # start the FPS counter
    fps = FPS().start()

    # loop over frames from the video file stream
    while True:
        # grab the frame from the threaded video stream and resize it
        # to 500px (to speedup processing)
        frame = vs.read()
        frame = imutils.resize(frame, width=500)
        # Detect the face boxes
        boxes = face_recognition.face_locations(frame)
        # compute the facial embeddings for each face bounding box
        encodings = face_recognition.face_encodings(frame, boxes)
        names = []

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
                    if currentname == 'Jordyn' and id==jordyn:
                        print("Access Granted, Jordyn")

                        vs.stop()
                        cv2.destroyAllWindows()
                        green_led_on()
                        countdown(5)

                    elif currentname == 'Enisha' and id==enisha:
                        print("Access Granted, Enisha")
                        countdown(5)
                        green_led_on()

                    elif currentname == 'Bryan' and id==bryan:
                        print("Access Granted, Bryan")
                        countdown(5)
                        green_led_on()

                    elif currentname == 'Jeremiah' and id==jeremiah:
                        print("Access Granted, Jeremiah")
                        countdown(5)
                        green_led_on()
                    else:
                        print("Denied Access")
                        main()

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
