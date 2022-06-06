import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img=cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)
"""
blank=np.zeros(img.shape[:2],dtype='uint8')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

mask=cv.bitwise_and(gray,gray,mask=circle)
cv.imshow('mask',mask)

#Grayscale histogram
grayHist=cv.calcHist([gray],[0],mask,[256],[0,256])"""

#Colour Histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('Quantities of pixels')
colors=('b','g','c')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)

#Em resumo, o histograma pode ser entendido como sendo um gráfico
#que irá indicar a quantidade de pixels em uma imagem