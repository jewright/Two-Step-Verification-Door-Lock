import cv2
import os

# Cascades Path
fCascPath = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_default.xml"
eCascPath = os.path.dirname(cv2.__file__) + "/data/haarcascade_eye.xml"
# Cascade Training
faceCascade = cv2.CascadeClassifier(fCascPath)
eyeCascade = cv2.CascadeClassifier(eCascPath)

# Opens Video Feed
# May need to switch value from between 0 and 1. Depends on the computer.
video_capture = cv2.VideoCapture(1)

while True:
  
    ret, frames = video_capture.read()
    # Convert to grayscale
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    
    # Detect faces and eyes
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=20, minSize=(30, 30),
                                         flags=cv2.CASCADE_SCALE_IMAGE)
    eyes = eyeCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=20, minSize=(30, 30),
                                       flags=cv2.CASCADE_SCALE_IMAGE)
    
    # Put a box around Face and Eyes that are detected. 
    for (x, y, w, h) in faces:
        cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 255, 0), 2)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(frames, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
    
    
    # Show number of faces and eyes detected on live feed. This is optional.
    font = cv2.FONT_HERSHEY_TRIPLEX
    x, y, w, h = 0, 0, 400, 50
    cv2.rectangle(frames, (x, x), (x + w, y + h), (0, 0, 0), -1)
    cv2.putText(frames, "Found {0} faces".format(len(faces)) + " and {0} eyes".format(len(eyes)),
                (x + int(w / 10), y + int(h / 1.5)), font, 0.7, (255, 255, 255), 2, 5)
    cv2.imshow('Faces and Eyes Detected', frames)
    
    # CLose video feed when q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
# Close Window 
video_capture.release()
cv2.destroyAllWindows()

# Final output of the last number of detected faces and eyes. This is optional
print("Found {0} faces".format(len(faces)) + " and {0} eyes".format(len(eyes))+"/n")


