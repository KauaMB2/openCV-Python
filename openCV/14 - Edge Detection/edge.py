import cv2 as cv
import numpy as np
img=cv.imread('Resources/Photos/park.jpg')
cv.imshow('park',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#Laplacion
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

#Sobel
solbelx=cv.Sobel(gray,cv.CV_64F,1,0)
solbely=cv.Sobel(gray,cv.CV_64F,0,1)
combinedSolbel=cv.bitwise_or(solbelx,solbely)
cv.imshow('Sobel X',solbelx)
cv.imshow('Sobel Y',solbely)
cv.imshow('combinedSolbel',combinedSolbel)

canny=cv.Canny(gray,150,175)
cv.imshow('Canny',canny)

cv.waitKey(0)