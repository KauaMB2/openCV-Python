import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)
# 1. Desenhar a imagem com uma cor específica
"""blank[:]=0,0,255
cv.imshow('Red',blank)
blank[:]=0,255,0
cv.imshow('Green',blank)
blank[:]=255,0,0
cv.imshow('Blue',blank)
blank[200:300,300:400]=0,255,0#Desenha só um pedaço
cv.imshow('Green2',blank)
cv.waitKey(0)"""

#2. Desenhando um retângulo
cv.rectangle(blank,(30,30),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=cv.FILLED)#cv.rectangle(imagem,(pontoDeOrigemX,pontoDeOrigemY),(tamamhoX,tamamhoY),(azul,verde,vermelho),thickness=valorDaEspessuraDaBorda)
cv.imshow('Rectangle',blank)

#3. Desenhando um circulo
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=10)#cv.circle(imagem,(pontoDeOrigemCentralX,pontoDeOrigemCentralY),raio,(tamanhoX,tamanhoY),(azul,verde,vermelho),thickness=valorDaEspessuraDaBorda)
cv.imshow('Circle',blank)

#4. Desenhando uma linha
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=3)#cv.line(imagem,(pontoDeOrigemX,pontoDeOrigemY),(pontoFinalX,pontoFinalY),(azul,verde,vermelho),thickness=valorDaEspessuraDaBorda)
cv.imshow('Line',blank)

#5. Escrevendo texto
cv.putText(blank,'Hello openCV! :)',(100,400),cv.FONT_HERSHEY_TRIPLEX,1.0,(225,255,255),2)#cv.putText(imagem,texto,(localX,localY),fonte,tamanhoDoTexto,(azul,verde,vermelho),espessura)
cv.imshow('Text',blank)
cv.waitKey(0)
