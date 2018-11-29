import cv2 as cv
import numpy as np

def extract_object_demo():
    capture =  cv.VideoCapture("E:/2.avi")
    while(True):
        ret, frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37,43,46])
        upper_hsv = np.array([77,255,255])
        mask = cv.inRange(hsv,lowerb = lower_hsv, upperb = upper_hsv)
        dst = cv.bitwise_and(frame,frame,mask = mask)
        cv.imshow("video",frame)
        cv.imshow("mask",dst)
        c = cv.waitKey(40)
        if c == 27:
            break

def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray image",gray)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow("hsv image",hsv)
    yuv = cv.cvtColor(image,cv.COLOR_BGR2YUV)
    cv.imshow("yuv image",yuv)
    ycrcb = cv.cvtColor(image,cv.COLOR_BGR2YCrCb)
    cv.imshow("ycrcb image",ycrcb)

src = cv.imread("E:\sample\lena(1).tiff")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

b,g,r = cv.split(src)
src = cv.merge([b+100,g,r])
cv.imshow("output image",src)
t1 = cv.getTickCount()
#extract_object_demo()
#color_space_demo(src)
#access_pixels(src)
extract_object_demo()
t2 = cv.getTickCount()
print("time:%ms",(t2-t1)/cv.getTickFrequency()*1000)
cv.waitKey(0) 
cv.destroyAllWindows()