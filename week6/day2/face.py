"""

Q2. Facial Recognition + OpenCV Python

Facial recognition is a biometric software application capable of uniquely identifying or verifying a person by comparing and analyzing.

Things that you need in this project: OpenCV and face_recognition

The project is mainly a method for detecting faces in a given image by using OpenCV-Python and face_recognition module. The first phase uses camera to capture the picture of our faces which generates a feature set in a location of your PC.

• The face_recognition command lets you recognize faces in a photograph or folder full for photographs.

It has two simple commands

Face_ recognition- Recognise faces in a photograph or folder full for photographs.
face_detection - Find faces in a photograph or folder full for photographs.
For face recognition, first generate a feature set by taking few image of your face and create a directory with the name of person and save their face image.


Then train the data by using the Face_ recognition module.By Face_ recognition module the trained data is stored as pickle file (.pickle).

By using the trained pickle data, we can recognize face.

The main flow of face recognition is first to locate the face in the picture and the compare the picture with the trained data set.If the there is a match, it gives the recognized label.
(Ref: https://github.com/sriram251/-face_recognition)
"""

import pandas as pd
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
#read the image and convert to grayscale format
img = cv.imread('rotated_face.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#calculate coordinates 
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    #draw bounding boxes around detected features
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#plot the image
plt.imshow(img)
#write image 
cv2.imwrite('face_detection.jpg',img)

