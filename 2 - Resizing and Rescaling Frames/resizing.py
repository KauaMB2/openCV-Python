import cv2 as cv

def rescaleFrame(frame, scale=0.2):
    #Imagens, videos e live videos
    height=int(frame.shape[0]*scale)# .shape[0] é referente á altura.
    width=int(frame.shape[1]*scale)#.shape[1] é referente á altura.
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
def changeRes(camera):
    #Apenas live video
    width=int(camera.shape[1])
    height=int(camera.shape[0])
    capture.set(3,width)
    capture.set(4,height)
img=cv.imread('Resources/Photos/cat.jpg')
imgResized=rescaleFrame(img)
cv.imshow('Cat',img)
cv.imshow('Cat Resized',imgResized)
capture=cv.VideoCapture('Resources/Videos/dog.mp4')
camera=cv.VideoCapture(0,cv.CAP_DSHOW)
while True:
    isTrue1,frame1=capture.read()
    isTrue2,frame2=camera.read()
    frameResized=rescaleFrame(frame1)
    changeRes(frame2)#NÃO FUNCIONAAAAAAAAAAA
    cv.imshow('Video',frame1)
    cv.imshow('Video Resized',frameResized)
    cv.imshow('Camera',frame2)
    if cv.waitKey(20) & 0xFF==ord('d'):#Se eu pressionar a tecla 'd', o vídeo encerra
        break
capture.release()#Encerra o vídeo
cv.destroyAllWindows()#Fecha todas as janelas abertas
