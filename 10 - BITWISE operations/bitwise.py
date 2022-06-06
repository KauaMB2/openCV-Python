import cv2 as cv
import numpy as np

blank=np.zeros((400,400),dtype='uint8')
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)

# bitwise AND --> Intersecting regions
bitwiseAnd=cv.bitwise_and(rectangle,circle)
cv.imshow('bitwiseAnd',bitwiseAnd)

# bitwise OR --> Non-intersecting regions Intersecting regions
bitwiseOr=cv.bitwise_or(rectangle,circle)
cv.imshow('bitwiseOr',bitwiseOr)

# bitwise XOR --> Non-insercting region
bitwiseXor=cv.bitwise_xor(rectangle,circle)
cv.imshow('bitwiseXor',bitwiseXor)

# bitwise NOT --> Invert the binary code
bitwiseNot=cv.bitwise_not(rectangle,circle)
cv.imshow('bitwiseNot',bitwiseNot)

cv.waitKey(0)