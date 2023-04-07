import cv2
import time

def faceDet():
   # Load the cascade
   face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

   # To capture video from webcam. 
   cap = cv2.VideoCapture(5)
   # To use a video file as input 
   # cap = cv2.VideoCapture('filename.mp4')

   while True:
       # Read the frame
       _, img = cap.read()
       start_time = time.time()
       # Convert to grayscale
       gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
       # Detect the faces
       faces = face_cascade.detectMultiScale(gray, 1.1, 4)
       print("--- %s Face Detection time for 1 image ---" % (time.time() - start_time))
       print("FPS: ", 1.0 / (time.time() - start_time))
       # Draw the rectangle around each face
       for (x, y, w, h) in faces:
           cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
       # Display
       cv2.imshow('img', img)
       # Stop if escape key is pressed
       k = cv2.waitKey(30) & 0xff
       if k==27:
           break
    # Release the VideoCapture object

faceDet()
