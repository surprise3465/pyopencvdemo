import cv2 as cv
import numpy as np
import os.path

def face_detect_demo(image, pathfile):
    if not os.path.isfile(pathfile):
        raise RuntimeError("%s: not found" % pathfile)
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    face_detector = cv.CascadeClassifier(pathfile)
    faces = face_detector.detectMultiScale(gray,scaleFactor = 1.13,minNeighbors = 2,flags = 0)
    for(x,y,w,h) in faces:
        cv.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
        # cv2.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)
        cv.imshow("Find Faces!",image)

def video_demo(pathfile):
    capture =  cv.VideoCapture("E:/2.avi")
    while(True):
        ret, frame = capture.read()
        cv.flip(frame,1)
        face_detect_demo(frame,path)
        c = cv.waitKey(10)
        if(c == 27):
            break

src = cv.imread('E:/sample/lena(1).tiff')
cv.namedWindow('input_image', cv.WINDOW_NORMAL)  #设置为WINDOW_NORMAL可以任意缩放
cv.imshow('input_image', src)
path = "E:\\workspace\\PyOpenCv\\haarcascade_frontalface_default.xml"
video_demo(path)
cv.waitKey(0)
cv.destroyAllWindows()