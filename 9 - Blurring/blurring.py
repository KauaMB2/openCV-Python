import cv2 as cv
img=cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

# Averaging
avarage=cv.blur(img,(3,3))
cv.imshow('Avarage Blur',avarage)

# Gaussian Blur
gauss=cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussian Blur',gauss)

# Median Blur
median=cv.medianBlur(img,7)
cv.imshow('medianBlur',median)

# Bilateral
bilateral=cv.bilateralFilter(img,1,15,15)
cv.imshow('bilateral',bilateral)



cv.waitKey(0)