import cv2 as cv
img=cv.imread('Resources/Photos/Cats.jpg')
cv.imshow('Cats',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#Limiar simples (Simple Thresholding)
threshold, thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Simple Thrasholding',thresh)

threshold, threshInv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple Thrasholding Inverse',threshInv)

#Limiar adaptativo(Adaptative Thrasholding)
adaptativeThresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptative Thrasholding Inverse',adaptativeThresh)

cv.waitKey(0)