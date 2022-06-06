import cv2 as cv
import numpy as np
img=cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('blank',blank)
blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
canny=cv.Canny(img, 125,175)
cv.imshow('canny edges',canny)
canny=cv.Canny(blur, 125,175)
cv.imshow('blur canny edges',canny)

#############################
ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

contourns, hierarchies=cv.findContours(thresh, cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contourns)} contornos encontrados!')#Quantidades de contornos
cv.drawContours(blank,contourns,-1,(0,0,255),1)
cv.imshow('contourns draw',blank)
cv.waitKey(0)