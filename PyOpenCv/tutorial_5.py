import cv2 as cv
import numpy as np

def fill_color_demo(image):
    copyImg = image.copy()
    h,w = image.shape[:2]
    mask = np.zeros([h+2,w+2],np.uint8)
    cv.floodFill(copyImg,mask,(30,30),(0,0,255),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo",copyImg)

def fill_binary_demo():
    image = np.zeros([400,400,3],np.uint8)
    image[100:300,100:300,:] = 255
    cv.imshow("fill_binary_demo",image)
    mask = np.ones([402,402,1],np.uint8)
    mask[101:402,101:402] = 0
    cv.floodFill(image,mask,(200,200),(100,2,255),cv.FLOODFILL_MASK_ONLY)
    cv.imshow("fill color demo",image)


src1 = cv.imread("E:\sample\lena(1).tiff")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src1)

#face = src1[220:400,180:360]
#gray = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
#backface = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
#src1[220:400,180:360] = backface
#cv.imshow("face image",src1)
#fill_color_demo(src1)
fill_binary_demo()
cv.waitKey(0) 
cv.destroyAllWindows()