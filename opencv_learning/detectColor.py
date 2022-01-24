import cv2
import numpy as np
from numpy.core.multiarray import result_type

def empty(v):
    pass

img = cv2.imread('mydog.jpg')
img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
# print(img.shape)
cv2.namedWindow('TrackBar')
cv2.resizeWindow('TrackBar', img.shape[1], img.shape[0])

cv2.createTrackbar('Hue Min', 'TrackBar', 0, 179, empty)
cv2.createTrackbar('Hue Max', 'TrackBar', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('Val Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Val Max', 'TrackBar', 255, 255, empty)

#hsv 為亮度,飽和度,色調的圖片相較於一般jpg更容易去過濾顏色
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while True:
    hue_min = cv2.getTrackbarPos('Hue Min', 'TrackBar')
    hue_max = cv2.getTrackbarPos('Hue Max', 'TrackBar')
    sat_min = cv2.getTrackbarPos('Sat Min', 'TrackBar')
    sat_max = cv2.getTrackbarPos('Sat Max', 'TrackBar')
    val_min = cv2.getTrackbarPos('Val Min', 'TrackBar')
    val_max = cv2.getTrackbarPos('Val Max', 'TrackBar')
    print(hue_min, hue_max, sat_min, sat_max, val_min, val_max)

    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask = cv2.inRange(hsv, lower, upper)
    result =cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('img',img)
    cv2.imshow('hsv',hsv)
    cv2.imshow('mask',mask)
    cv2.imshow('result',result)
    cv2.waitKey(1)