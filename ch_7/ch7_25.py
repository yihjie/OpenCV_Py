# 使用 3 個滾動條設計影像背景顏色
# 按 ESC ( key == 27 ) 離開

import cv2
import numpy as np


def onChange(x):
    b = cv2.getTrackbarPos("B", 'canvas')  # 建立 B 通道 藍色
    g = cv2.getTrackbarPos("G", 'canvas')  # 建立 G 通道 綠色
    r = cv2.getTrackbarPos("R", 'canvas')  # 建立 R 通道 紅色
    canvas[:] = [b, g, r]  # 設定背景色


canvas = np.ones((300, 640, 3), np.uint8) * 255

cv2.namedWindow("canvas")

cv2.createTrackbar("B", "canvas", 0, 255, onChange)
cv2.createTrackbar("G", "canvas", 0, 255, onChange)
cv2.createTrackbar("R", "canvas", 0, 255, onChange)

while 1:
    cv2.imshow("canvas", canvas)
    key = cv2.waitKey(100)  # 0.1 秒檢查一次
    if key == 27:
        break

cv2.destroyAllWindows()
