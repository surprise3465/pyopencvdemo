import cv2 as cv
import numpy as np
 
def hat_demo(img):
    """顶帽/黑帽梯度"""
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)
    cv.imshow("topHat", dst)
 
    dst = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel)
    cv.imshow("blackHat", dst)
 
 
def base_demo(img):
    """基本梯度"""
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.morphologyEx(gray, cv.MORPH_GRADIENT, kernel)
    cv.imshow("base", dst)
 
 
def i_e_demo(img):
    """内/外梯度"""
    kerenl = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dm = cv.dilate(img, kerenl)
    em = cv.erode(img, kerenl)
    # 内梯度
    dst1 = cv.subtract(img, em)
    # 外梯度
    dst2 = cv.subtract(dm,img)
    cv.imshow("intrenal", dst1)
    cv.imshow("external", dst2)
 

src = cv.imread('E:/sample/lena(1).tiff')
cv.namedWindow('input_image', cv.WINDOW_NORMAL)  #设置为WINDOW_NORMAL可以任意缩放
cv.imshow('input_image', src)
hat_demo(src)
base_demo(src)
i_e_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
