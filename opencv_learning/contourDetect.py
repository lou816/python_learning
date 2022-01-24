import cv2

img = cv2.imread('shape.jpg')

#複製一張圖片出來
imgContour = img.copy()

#轉灰階來辨識輪廓
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img, 150, 200)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 4)
    # print(cv2.contourArea(cnt))
    area = cv2.contourArea(cnt)
    # print(cv2.arcLength(cnt, True,))
    if area>500:
        peri = cv2.arcLength(cnt, True)
        #找出頂點位置
        vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)
        corners = len(vertices)
        x, y, w, h = cv2.boundingRect(vertices)
        cv2.rectangle(imgContour, (x,y), (x+w,y+h), (0,255,0), 4)
        if corners == 3:
            cv2.putText(imgContour, 'triangle', (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)
        elif corners == 4:
            cv2.putText(imgContour, 'rectangle', (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)
        elif corners == 5:
            cv2.putText(imgContour, 'pentagon', (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)
        elif corners >= 6:
            cv2.putText(imgContour, 'circle', (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)

cv2.imshow('img',img)
cv2.imshow('canny',canny)
cv2.imshow('imgcontour', imgContour)
cv2.waitKey(0)