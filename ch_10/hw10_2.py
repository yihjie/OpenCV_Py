# 同時進行影像的水平和垂直翻轉
# Modified from ch10_14.py and ch10_15.py

import cv2
import numpy as np

src = cv2.imread('huang.jpg')

rows, cols = src.shape[:2]
mapX = np.zeros(src.shape[:2], np.float32)
mapY = np.zeros(src.shape[:2], np.float32)

for r in range(rows):
    for c in range(cols):
        mapX.itemset((r, c), cols - 1 - c)  # 水平鏡射
        mapY.itemset((r, c), rows - 1 - r)  # 垂直鏡射

dst = cv2.remap(src, mapX, mapY, cv2.INTER_LINEAR)

cv2.imshow('Src', src)
cv2.imshow('Dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
