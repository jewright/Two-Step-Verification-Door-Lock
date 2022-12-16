#! /usr/bin/python

# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2


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

    # current name only triggers when a person is identified
    currentname = "unknown"
    # Determine faces from encodings.pickle which is our trained model
    encodingsP = "encodings.pickle"

    print("[INFO] loading encodings + face detector...")
    data = pickle.loads(open(encodingsP, "rb").read())

    # src = camera feed
    vs = cv2.VideoCapture(0)
    vs.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    vs.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

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
                    if currentname == 'Jordyn':
                        print("Access Granted, Jordyn")
                        vs.release()
                        # do a bit of cleanup
                        cv2.destroyAllWindows()
                        countdown(5)

                    if currentname == 'Enisha':
                        print("Access Granted, Enisha")
                    if currentname == 'Bryan':
                        print("Access Granted, Bryan")
                        vs.release()
                        # do a bit of cleanup
                        cv2.destroyAllWindows()
                        countdown(5)
                    if currentname == 'Jeremiah':
                        print("Access Granted, Jeremiah")

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

    cv2.release()
    # do a bit of cleanup
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
