import cv2 as cv
import numpy as np

def contours_demo(image):
    dst = cv.GaussianBlur(image, (3, 3), 0) #高斯模糊去噪
    gray = cv.cvtColor(dst, cv.COLOR_RGB2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU) #用大律法、全局自适应阈值方法进行图像二值化
    cv.imshow("binary image", binary)
    cloneTmage, contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), 2)
        print(i)
    cv.imshow("contours", image)
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), -1)
    cv.imshow("pcontours", image)

src = cv.imread('E:/imageload/coins.jpg')
cv.namedWindow('input_image', cv.WINDOW_NORMAL) #设置为WINDOW_NORMAL可以任意缩放
cv.imshow('input_image', src)
contours_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()