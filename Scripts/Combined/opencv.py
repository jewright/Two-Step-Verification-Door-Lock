import cv2
import os

vs = cv2.VideoCapture(1)

while True:
    ret, frame = vs.read()
    cv2.imshow('', frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()
