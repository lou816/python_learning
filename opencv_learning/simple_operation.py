import cv2
import numpy as np
import random
#創建圖片可使用numpy
#empty((寬pix, 高pix, rgb), 顏色bit數)

img =cv2.imread('mydog.jpg')
# print(img.shape)

#以下是一張全彩圖片建立
# img = np.empty((300, 300, 3), np.uint8)


#將部分區塊改成隨機顏色
# for row in range(300):
#     for col in range(img.shape[1]):
#         img[row][col] = [ random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]# B, G, R

#以下為取得部分圖片內容的方式
newImg = img[ :150, 200:400]

cv2.imshow('img', img)
cv2.imshow('newImg', newImg)
cv2.waitKey(0)

# simple image form
# [
#     [[B,G,R],[B,G,R],[B,G,R]...960],
#     [[B,G,R],[B,G,R],[B,G,R]...960],
#     [[],[],[]...960],
#     [[],[],[]...960],
#     ...1706
# ]