import cv2 as cv
import numpy as np
img=cv.imread('Resources/Photos/group 1.jpg')
cv.imshow('Group',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Group Gray',gray)

haarCascade=cv.CascadeClassifier('filesXML/haar_face.xml')
facesRect=haarCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)
print(f'Numbers of faces found in image: {(len(facesRect))}')
for (x,y,w,h) in facesRect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Faces',img)


cv.waitKey(0)