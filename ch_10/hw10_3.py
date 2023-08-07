# remap() 逆時鐘轉90度

import cv2
import numpy as np

src = cv2.imread('hung_square.jpg')

rows, cols = src.shape[:2]
mapX = np.zeros(src.shape[:2], np.float32)
mapY = np.zeros(src.shape[:2], np.float32)

for r in range(rows):
    for c in range(cols):
        mapX.itemset((r, c), rows - 1 - r)
        mapY.itemset((r, c), c)

dst = cv2.remap(src, mapX, mapY, cv2.INTER_LINEAR)

cv2.imshow('Src', src)
cv2.imshow('Dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
