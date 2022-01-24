#基本 opencv操作
#imread( '檔名') 讀取圖片 return image
#imshow( '視窗名稱', 圖片變數) 打印在螢幕 
#waitKey( 秒數) 等待輸入 return keyValue
#resize( 圖片變數, ( 寬pix, 高pix), fx=寬倍率縮放, fy=高倍率縮放) return image
#VideoCapture( '檔名') 讀取影片 return video
#read() 讀取一幀 return bool img
import cv2
# img = cv2.imread('mydog.jpg')
# cv2.imshow('this is img',img)
ret = True
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0,0), fx=0.4, fy=0.4)
    if ret:
        cv2.imshow('this is video',frame)
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        break


