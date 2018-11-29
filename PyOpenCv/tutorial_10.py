import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def equalHist_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow("equalHist_demo",dst)

def clahe_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit = 2.0, tileGridSize = (8,8))
    dst = clahe.apply(gray)
    cv.imshow("clahe_demo",dst)

def creat_rgb_hist(image):
    h, w, c = image.shape
    rgbHist = np.zeros([16*16*16, 1], np.float)#np.float32
    binsize = 256/16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b/binsize)*16*16 + np.int(g/binsize)*16 + np.int(r/binsize)
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] +1
    return rgbHist

def hist_compare(image1, image2):
    hist1 = creat_rgb_hist(image1)
    hist2 = creat_rgb_hist(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print("巴氏距离:{}\n 相关距离:{}\n 卡方距离:{}\n".format(match1, match2, match3))

src1 = cv.imread("E:\sample\lena.tiff")
src2 = cv.imread("E:\sample\lena.tiff")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src1)
cv.imshow("input image2",src2)
t1 = cv.getTickCount()

#equalHist_demo(src1)
#clahe_demo(src1)
hist_compare(src1,src2)
t2 = cv.getTickCount()
print("time:%ms",(t2-t1)/cv.getTickFrequency()*1000)
cv.waitKey(0) 
cv.destroyAllWindows() 