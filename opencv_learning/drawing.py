import cv2
import numpy as np

#圖片的表達 (高,寬,層)

img = np.zeros((600, 800, 3), np.uint8)
# print(img.shape)
#劃一條線 from x=0,y=0 to x=400,y=300
cv2.line(img, (0,0), (400,300), (255, 0 ,0), 10)
#劃一個矩形 from x=0,y=0 to x=400,y=300
cv2.rectangle(img , (0,0), (400, 300), (0, 0, 255), 20, cv2.FILLED)
#劃一個圓形
cv2.circle(img, (600,400), 10, (0,255,0), 3, cv2.FILLED)
#畫上文字
cv2.putText(img, "123", (100,500), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,255,255), 5)



cv2.imshow('img', img)

cv2.waitKey(0)