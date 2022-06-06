import cv2 as cv
import numpy as np

img=cv.imread('Resources/Photos/park.jpg')
cv.imshow('Boston',img)

# Transladando imagens
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
# -x --> Left
# -y --> Up
# x --> Right
# y --> Down
translated=translate(img,100,100)
cv.imshow('translated',translated)

# Rotação
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)
rotated=rotate(img,-45)
cv.imshow('rotated',rotated)
rotated_rotated=rotate(rotated,-45)
cv.imshow('rotated rotated',rotated_rotated)

# Redimencionar
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

# Virando
flip=cv.flip(img,-1)
cv.imshow('flip',flip)

# Cortar
cropped=img[200:400,100:400]
cv.imshow('croppped',cropped)




cv.waitKey(0)