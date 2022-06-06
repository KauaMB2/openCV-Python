import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('Resources/Photos/park.jpg')
cv.imshow('park',img)
plt.imshow(img)
plt.show()

# Escala cinza
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# Inversão de cores
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

# BGR to L*A*B
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

#Convertendo BGR par RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)


#Não é possível converter grayscale to HSV de forma direta...
#Primeiramente, é necessário converter o grayscale para BGR e após isso, converter para HSV

plt.imshow(rgb)
plt.show()
cv.waitKey(0)