import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def plot_demo(image):
    plt.hist(image.ravel(), 255)
    # plt.hist(image.ravel(), 255, range=[0, 256])
    plt.show("直方图")

def image_demo(image):
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        hist = cv.calcHist([image], channels=[i], mask=None, histSize=[256], ranges=[0, 255])
        plt.plot(hist, color=color)
        plt.xlim([0, 255])
        # plt.xticks() 设置x轴刻度的表现方式
        # plt.xlim() 设置x轴刻度的取值范围
    plt.show("图像直方图")

src1 = cv.imread("E:\sample\lena(1).tiff")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src1)
t1 = cv.getTickCount()

plot_demo(src1)
image_demo(src1)
t2 = cv.getTickCount()
print("time:%ms",(t2-t1)/cv.getTickFrequency()*1000)
cv.waitKey(0) 
cv.destroyAllWindows() 