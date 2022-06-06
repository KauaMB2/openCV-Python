import cv2 as cv
img=cv.imread('Resources/Photos/park.jpg')
cv.imshow('Boston',img)

#1 - Convertendo para a escala cinza
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#2 - Borrão(Blur)
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#3 - Cascata de borda(Edge Cascate)
imgEdge=cv.Canny(img,125,175)
cv.imshow('imgEdge',imgEdge)
blurEdge=cv.Canny(blur,125,175)
cv.imshow('blurEdge',blurEdge)

#4 - Dilatando a imagem
dilated=cv.dilate(blurEdge,(3,3),iterations=3)
cv.imshow('dilated',dilated)

#5 - Eroding
eroded=cv.erode(img,(7,7),iterations=3)
cv.imshow('eroded',eroded)

#6 - Reajuste de tamanho
resized=cv.resize(img,(100,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

#7 - Cortar imagens
cropped=img[50:200,200:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)


