import cv2
import numpy as np

kernel = np.ones((10, 10), np.uint8)
kernel1 = np.ones((10, 10), np.uint8)

img = cv2.imread( 'mydog.jpg')
img = cv2.resize( img, ( 0, 0), fx=0.2, fy=0.2)

#彩色圖片轉灰階 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#圖片模糊
blur = cv2.GaussianBlur( img, ( 3, 3), 0)
#取得圖片邊緣
canny = cv2.Canny( img, 150, 200)
#圖片膨脹 => 線條變粗
dilate = cv2.dilate( canny, kernel, iterations=2)
#圖片侵蝕 => 線條變細
erode = cv2.erode( dilate, kernel1, iterations=5)

# cv2.imshow( 'img', img)
# cv2.imshow( 'grayImg', gray)
# cv2.imshow( 'blurImg', blur)
cv2.imshow( 'cannyImg', canny)
cv2.imshow( 'dilateImg', dilate)
cv2.imshow( 'erodeImg', erode)
cv2.waitKey(0)
