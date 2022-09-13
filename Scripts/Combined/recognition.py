import cv2
import numpy as np
import os
from timer import countdown
from led import green_led_on, green_led_off, red_led_off, red_led_on


def rec():
    green_led_on()

    print("Checking Face...")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('/home/pi/Scripts/facial_recognition/trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);

    font = cv2.FONT_HERSHEY_SIMPLEX

    # initialize id
    id = 0

    # names related to ids: example ==> Marcelo: id=1, etc
    names = ['None', 'Jordyn']

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video widht
    cam.set(4, 480)  # set video height

    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(int(minW), int(minH)), )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):
                id = names[id]
                confidence = round(100 - confidence)
                print(id, confidence)
                if (confidence < 45):
                    green_led_off()
                    red_led_on()

                elif (confidence > 45):
                    red_led_off()
                    green_led_on()
                    print("You have 10 seconds to enter.")
                    countdown(10)
                    if countdown(0):
                        break






            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
            # cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            # cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
        # cv2.imshow('camera', img)

    print("\n [INFO] Exiting Program")
    cam.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()
