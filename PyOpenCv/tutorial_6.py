import cv2 as cv
import numpy as np

def blur_demo(image):
    dst = cv.blur(image,(5,5))
    cv.imshow("blur_demo",dst)


def median_blur_demo(image):
    dst = cv.medianBlur(image,5)
    cv.imshow("median_blur_demo",dst)

def custom_blur_demo(image):
    #kernel =np.ones([5,5],np.float)/25
    kernel =np.array([[0,-2,0],[-1,5,-1],[0,-2,0]],np.float)
    dst = cv.filter2D(image,-1,kernel = kernel)
    cv.imshow("custom_blur_demo",dst)

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
#blur_demo(src1)
#median_blur_demo(src1)
#custom_blur_demo(src1)
gaussian_demo(src1)
dst = cv.GaussianBlur(src1,(5,5),5)
cv.imshow("GaussianBlur",dst)
t2 = cv.getTickCount()
print("time:%ms",(t2-t1)/cv.getTickFrequency()*1000)
cv.waitKey(0) 
cv.destroyAllWindows()