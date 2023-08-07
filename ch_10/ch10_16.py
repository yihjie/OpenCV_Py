# 水平翻轉
'''
使用 remap()
map1 (mapX) : cols - 1 - c
map2 (mapY) : 不變
'''

import cv2
import numpy as np

src = cv2.imread('huang.jpg')

rows, cols = src.shape[:2]
mapX = np.zeros(src.shape[:2], np.float32)
mapY = np.zeros(src.shape[:2], np.float32)

for r in range(rows):
    for c in range(cols):
        mapX.itemset((r, c), cols - 1 - c)  # 水平鏡射
        mapY.itemset((r, c), r)

dst = cv2.remap(src, mapX, mapY, cv2.INTER_LINEAR)

cv2.imshow('Src', src)
cv2.imshow('Dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
