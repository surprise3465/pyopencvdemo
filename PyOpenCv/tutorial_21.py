import cv2 as cv
import numpy as np


def contours_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    ret, binary = cv.threshold(
        gray, 0, 255,
        cv.THRESH_BINARY | cv.THRESH_OTSU)  #用大律法、全局自适应阈值方法进行图像二值化
    cv.imshow("binary image", binary)
    cloneTmage, contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL,
                                                     cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)
        x, y, w, h = cv.boundingRect(contour)
        mm = cv.moments(contour)
        cx = mm['m10'] / mm['m00']
        cy = mm['m01'] / mm['m00']
        cv.circle(image, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        approxCurve = cv.approxPolyDP(contour, 4, True)
        print(approxCurve.shape)
        if (approxCurve.shape[0] > 6):
            cv.drawContours(image, contours, i, (255, 0, 0), 2)
        if (approxCurve.shape[0] == 4):
            cv.drawContours(image, contours, i, (0, 255, 0), 2)
        if (approxCurve.shape[0] == 3):
            cv.drawContours(image, contours, i, (0, 0, 255), 2)
    cv.imshow("contours_demo", image)


src = cv.imread('E:/sample/patterns.png')
cv.namedWindow('input_image', cv.WINDOW_NORMAL)  #设置为WINDOW_NORMAL可以任意缩放
cv.imshow('input_image', src)
contours_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()