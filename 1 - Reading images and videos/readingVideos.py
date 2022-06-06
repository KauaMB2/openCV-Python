import cv2 as cv
capture=cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue,frame=capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):#Se eu pressionar a tecla 'd', o vídeo encerra
        break
capture.release()#Encerra o vídeo
cv.destroyAllWindows()#Fecha todas as janelas abertas