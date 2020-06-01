import cv2
import os
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
#Load the classifier
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#For each individual, enter a face id like 1,2,3,...
faceID = input('\n Enter user id and press ENTER: ')
print("\n Initializing... Look at the camera!")
#Initialize individual sampling face count
count = 0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count += 1
        # Save the captured image into the faceSampleMany folder
        cv2.imwrite("faceSampleMany/User." + str(faceID) + '.' + str(count) + ".jpg", gray[y:y+h, x:x+w])
        cv2.imshow('image', img)


    k = cv2.waitKey(100) & 0xff # Press 'Esc' button to exit
    if k == 27:
        break
    elif count >= 150: # Take 150 face sample and stop
        break
# Cleaning up!
cam.release()
cv2.destroyAllWindows()
    

    
                
