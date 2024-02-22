import cv2
import numpy as np
import face_recognition
import os

path = "ImagesAttendance"
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:

    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
    print(classNames)
def findEncodings(images):
    encodeList=[]
    for img in images:
        #print("img",type(img))
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encoding = face_recognition.face_encodings(img)[0]
        encodeList.append(encoding)
        return encodeList
cv2.imshow('Webcam',img)
cv2.waitKey(1)