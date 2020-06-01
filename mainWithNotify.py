# -*- coding: utf-8 -*-
"""
Created on Mon April 20 19:44:21 2020

@author: Alain Honore Kubwayo 
"""
 
import cv2
import smtplib
import numpy as np
import matplotlib.pyplot as plt
from os.path import isfile, join
from os import listdir 

#Provide the Path to the folder where the sample faces collected from running "sampleCollection.py" are saved
pathTrain ='C:/ASHESI UNIVERSITY COLLEGE/FR-Version1/faceSample/'  
file = [f for f in listdir(pathTrain) if isfile(join(pathTrain,f))]

trainingData, labels = [], []

for i, files in enumerate(file):
    trainImagePath = pathTrain + file[i]
    images = cv2.imread(trainImagePath, cv2.IMREAD_GRAYSCALE)
    trainingData.append(np.asarray(images, dtype=np.uint8))
    labels.append(i)

labels = np.asarray(labels, dtype=np.int32)

#The LBPH Recognizer
model = cv2.face.LBPHFaceRecognizer_create()

model.train(np.asarray(trainingData), np.asarray(labels))

#Wait for few seconds for training to complete!
print(">>>>>>>>>>>>>>>>>")
print("Training Complete")
print(">>>>>>>>>>>>>>>>>")

#Load the Haar-cascades Classifier stored in the main directory
cascade_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect(img, size = 0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade_classifier.detectMultiScale(gray, 1.3, 5)
    
    if faces is(): 
        return img,[] 

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200,200))

    return img,roi

acc = []

cap = cv2.VideoCapture(0)
while True:

    ret, frame = cap.read()

    image, face = detect(frame)

    try: 
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        res = model.predict(face)

        #Calculating accuracy
        if res[1] < 100:
            confidence = float("{0:.2f}".format((100*(1-(res[1])/300))))

            acc.append(confidence)
            dis = str(confidence)

        font = cv2.FONT_HERSHEY_DUPLEX
        name = dis
        color = (0, 255, 0)
        stroke = 2
        cv2.putText(image, name, (100,120), font, 1, color, stroke)
        
        cv2.imshow('Face Window', image)

        #Access Control: Door gets unlocked for accuracy of 80% and above
        if confidence > 80:
            font = cv2.FONT_HERSHEY_DUPLEX
            name = "Door Unlocked"
            color = (0, 255, 0)
            stroke = 2
            cv2.putText(image, name, (250, 450), font, 1, color, 2)
            cv2.imshow('Face Window', image)
            
            print("Face Detected and Recognized! Sending Notification... ")
            #Notification Code 
            senderEmail = "accesscontrolnotify@gmail.com"
            receiverEmail = "ahkubwayo@gmail.com"
            
            password = "reum jabo tecy tfbe"
            subject = 'Access Control Notification'
            message = "Access Granted!"
            header='To: ' + receiverEmail + '\n' + 'From: ' + senderEmail + '\n' + 'Subject: ' + subject
            
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(senderEmail, password)
            print("Login successful!")
            server.sendmail(senderEmail, receiverEmail, header + '\n\n'+ message)
            print("Email has been sent to ", receiverEmail)
            #End of Notification Code

            
        else:
            #Access Control: Door remains locked for accuracy below 80%
            font = cv2.FONT_HERSHEY_DUPLEX
            name = "Door Locked"
            color = (0, 0, 255)
            stroke = 2
            cv2.putText(image, name, (250, 450), font, 1, color, 2)
            cv2.imshow('Face Window', image)
            
            
            print("Face Detected but Unrecognized! Sending Notification... ")
            #Notification Code 
            senderEmail = "accesscontrolnotify@gmail.com"            #System will send email from this email
            receiverEmail = "ahkubwayo@gmail.com"                    #Replace email with your email
            
            password = "reum jabo tecy tfbe"                         #App password for the system email
            subject = 'Access Control Notification'
            message = "Access Denied!"
            header='To: ' + receiverEmail + '\n' + 'From: ' + senderEmail + '\n' + 'Subject: ' + subject
            
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(senderEmail, password)
            print("Login successful!")
            server.sendmail(senderEmail, receiverEmail, header + '\n\n'+ message)
            print("Email has been sent to ", receiverEmail)
            #End of Notification Code

    except:
        print("No Face Detected!")
        font = cv2.FONT_HERSHEY_DUPLEX
        name = "No Face Detected"
        color = (255, 0, 0)
        stroke = 2
        cv2.putText(image, name, (250, 450), font, 1, color, 2)
        cv2.imshow('Face Window', image)
        pass
    #To exit, press q button on keyboard
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

print(acc)
print('Highest Accuracy Generated: ' + str((np.max(acc))))
print("---------------------------------------------------")

plt.plot(acc)
plt.ylabel('Accuracy')
plt.xlabel('Run Time')
plt.title('Confidence Plot')
plt.show()

cap.release()
cv2.destroyAllWindows()
