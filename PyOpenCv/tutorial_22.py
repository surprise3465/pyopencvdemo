import cv2 as cv
import numpy as np

def erode_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    ret, binary = cv.threshold(gray, 0, 255,cv.THRESH_BINARY | cv.THRESH_OTSU)  #用大律法、全局自适应阈值方法进行图像二值化
    kernel = cv.getStructuringElement(cv.MORPH_RECT ,(15,15))
    dst = cv.erode(binary,kernel)
    cv.imshow("erode_demo", dst)

def dilate_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    ret, binary = cv.threshold(gray, 0, 255,cv.THRESH_BINARY | cv.THRESH_OTSU)  #用大律法、全局自适应阈值方法进行图像二值化
    kernel = cv.getStructuringElement(cv.MORPH_RECT ,(15,15))
    dst = cv.dilate(binary,kernel)
    cv.imshow("dilate_demo", dst)

src = cv.imread('E:/sample/lena(1).tiff')
cv.namedWindow('input_image', cv.WINDOW_NORMAL)  #设置为WINDOW_NORMAL可以任意缩放
cv.imshow('input_image', src)
kernel = cv.getStructuringElement(cv.MORPH_RECT ,(5,5))
dst = cv.erode(src,kernel)
cv.imshow("erode_demo", dst)

dst = cv.dilate(src,kernel)
cv.imshow("dilate_demo", dst)
#erode_demo(src)
#dilate_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()