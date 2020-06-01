# -*- coding: utf-8 -*-
"""
Created on Mon April 20 18:00:00 2020

@author: Alain Honore Kubwayo
"""

import numpy as np
import cv2

#Loading the Haar-cascade classifier
cascadeClassifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def extract(img):

    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascadeClassifier.detectMultiScale(grayImage, scaleFactor=1.5, minNeighbors=5)

    if faces is ():
        return None

    for (x,y,w,h) in faces:
        crop = img[y:y+h, x:x+w]
    return crop

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if extract(frame) is not None:
        count += 1
        face = cv2.resize(extract(frame),(200,200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        #Store the faces being captured into "faceSample" folder created inside the project folder
        path = 'faceSample/usr'+str(count)+'.jpg'
        cv2.imwrite(path, face)
        name = str(count)
        font = cv2.FONT_HERSHEY_DUPLEX
        color = (0,255,0) 
        stroke = 2
        cv2.putText(face, name, (50,50), font, 1, color, stroke)
        cv2.imshow('Face Window', face)
    else:
        print("Error: No Face")
        pass
    
    if cv2.waitKey(20) & 0xFF == ord('q') or count==150:
        break

print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
print("Sample collection complete")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>")

cap.release()
cv2.destroyAllWindows()
