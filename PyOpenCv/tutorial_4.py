import cv2 as cv
import numpy as np

def add_demo(m1,m2):
    dst = cv.add(m1,m2)
    cv.imshow("add_demo",dst)


def divide_demo(m1,m2):
    dst = cv.divide(m1,m2)
    cv.imshow("divide_demo",dst)


def subtract_demo(m1,m2):
    dst = cv.subtract(m1,m2)
    cv.imshow("subtract_demo",dst)


def multiply_demo(m1,m2):
    dst = cv.multiply(m1,m2)
    cv.imshow("multiply_demo",dst)

def logic_demo(m1,m2):
    dst = cv.bitwise_xor(m1,m2)
    cv.imshow("logic_demo",dst)

def contrast_brightness_demo(image,c,b):
    h,w,ch = image.shape
    blank = np.zeros([h,w,ch],image.dtype)
    dst = cv.addWeighted(image,c,blank,1-c,b)
    cv.imshow("contrast_brightness_demo",dst)

src1 = cv.imread("E:\sample\lena(1).tiff")
src2 = cv.imread("E:\sample\lena.tiff")

cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src1)
t1 = cv.getTickCount()
contrast_brightness_demo(src1,1.5,0)
t2 = cv.getTickCount()
print("time:%ms",(t2-t1)/cv.getTickFrequency()*1000)
cv.waitKey(0) 
cv.destroyAllWindows()