import cv2 as cv
import numpy as np
 
def open_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    #形态学操作
    #第二个参数：要执行的形态学操作类型，这里是开操作
    binary=cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)
    cv.imshow("open_demo",binary)
 
def close_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    #形态学操作
    #第二个参数：要执行的形态学操作类型，这里是开操作
    binary=cv.morphologyEx(binary,cv.MORPH_CLOSE,kernel)
    cv.imshow("close_demo",binary)

src = cv.imread('E:/sample/python.png')
cv.namedWindow('input_image', cv.WINDOW_NORMAL)  #设置为WINDOW_NORMAL可以任意缩放
cv.imshow('input_image', src)
open_demo(src)
close_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
