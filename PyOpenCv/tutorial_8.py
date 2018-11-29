import cv2 as cv
import numpy as np


def bi_demo(image):
    dst = cv.bilateralFilter(src=image, d=0, sigmaColor=100, sigmaSpace=15)
    cv.imshow("bi_demo", dst)

def mean_shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(src=image, sp=15, sr=50)
    cv.imshow("mean_shift image", dst)

def clamp(pv):
    if pv>255 :
        return 255
    if pv<0 :
        return 0
    else:
        return pv

def gaussian_demo(image):
    h,w,ch = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0,20,3)
            b = image[row,col,0]
            g = image[row,col,1]
            r = image[row,col,2]
            image[row,col,0] = clamp(b+s[0])
            image[row,col,1] = clamp(g+s[1])
            image[row,col,2] = clamp(r+s[2])

    cv.imshow("gaussian_demo",image)


src1 = cv.imread("E:\sample\lena(1).tiff")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src1)
t1 = cv.getTickCount()
gaussian_demo(src1)
mean_shift_demo(src1)
t2 = cv.getTickCount()
print("time:%ms",(t2-t1)/cv.getTickFrequency()*1000)
cv.waitKey(0) 
cv.destroyAllWindows()