import cv2 as cv
import numpy as np

def access_pixels(image):
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print(image.shape[0])
    print(image.shape[1])
    print(image.shape[2])
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row,col,c]
                image[row,col,c] = 255-pv
    cv.imshow("image show",image)

def create_image():
    img = np.zeros([400,400,3],np.uint8)
    img[:,:,0] = np.ones([400,400])*111
    img[:,:,1] = np.ones([400,400])*222
    img[:,:,2] = np.ones([400,400])*127
    cv.imshow("new image",img)

def invers_image(image):
    dst = cv.bitwise_not(image)
    cv.imshow("verse image",dst)

src = cv.imread("E:\lena(1).tiff")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
t1 = cv.getTickCount()
invers_image(src)
#access_pixels(src)
t2 = cv.getTickCount()
print("time:%ms",(t2-t1)/cv.getTickFrequency()*1000)
cv.waitKey(0)
cv.destroyAllWindows()