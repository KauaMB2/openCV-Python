import cv2 as cv
import numpy as np
img=cv.imread('Resources/Photos/park.jpg')
blank=np.zeros(img.shape[:2],dtype='uint8')

#Separando os canais de cores...    cv.split()
b,g,r=cv.split(img)
cv.imshow('b',b)
cv.imshow('g',g)
cv.imshow('r',r)

# Mesclando canais de cores...   cv.marged([,,])
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged=cv.merge([b,g,r])
cv.imshow('merged',merged)

cv.waitKey(0)