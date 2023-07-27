# Modified ch7_4.py

import cv2
import numpy as np

img = cv2.imread('antarctic.jpg')                       # 使用影像當畫布
#img[1:300, 1:300] = (0, 255, 255)                       # B=0, G=255, R=255 == Yellow

cy = int(img.shape[0] / 2)  # 圖片中心點的 Y 座標
cx = int(img.shape[1] / 2)  # 圖片中心點的 X 座標

lx = cx - 150
rx = cx + 150
uy = cy - 150
ly = cy + 150


cv2.line(img, (lx, uy), (rx, uy), (255, 0, 0))        # 上方水平直線
cv2.line(img, (lx, ly), (rx, ly), (255, 0, 0))        # 下方水平直線
cv2.line(img, (rx, uy), (rx, ly), (255, 0, 0))        # 右方垂直直線
cv2.line(img, (lx, uy), (lx, ly), (255, 0, 0))        # 左方垂直直線

for x in range(cx, rx, 10):
    cv2.line(img, (x, uy), (rx, x - cy), (255, 0, 0))  # 右上角斜線

for y in range(cy, ly, 10):
    cv2.line(img, (lx, y), (lx + y - cy, ly), (255, 0 ,0))  # 左下角斜線

cv2.imshow("My Draw", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
