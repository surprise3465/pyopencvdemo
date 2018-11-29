import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def hist2d_demo(image):
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    hist = cv.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
    #cv.imshow("hist2d_demo",hist)
    plt.imshow(hist,interpolation="nearest")
    plt.title("hist2d_demo")
    plt.show()

def back_projection_demo():
    sample = cv.imread("E:/sample/fruits_section.jpg")
    target = cv.imread("E:/sample/fruits.jpg")

    roi_hsv = cv.cvtColor(sample,cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target,cv.COLOR_BGR2HSV)

    cv.imshow("sample",sample)
    cv.imshow("target",target)

    roihist = cv.calcHist([roi_hsv],[0,1],None,[180,256],[0,180,0,256])
    cv.normalize(roihist, roihist, 0, 255, cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv],[0,1],roihist,[0,180,0,256],1)
    cv.imshow("target",dst)

src1 = cv.imread("E:\sample\lena(1).tiff")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src1)
t1 = cv.getTickCount()
hist2d_demo(src1)
back_projection_demo()
t2 = cv.getTickCount()
print("time:%ms",(t2-t1)/cv.getTickFrequency()*1000)
cv.waitKey(0) 
cv.destroyAllWindows() 