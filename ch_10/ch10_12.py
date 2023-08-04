# 影像複製
# dst = cv2.remap(src, map1, map2, interpolation, borderMode, borderValue)

import cv2
import numpy as np

src = cv2.imread('huang.jpg')

rows, cols = src.shape[:2]

mapX = np.zeros(src.shape[:2], np.float32)
mapY = np.zeros(src.shape[:2], np.float32)

for r in range(rows):
    for c in range(cols):
        mapX.itemset((r, c), c)
        mapY.itemset((r,c), r)

dst = cv2.remap(src, mapX, mapY, cv2.INTER_LINEAR)

cv2.imshow('Src', src)
cv2.imshow('Dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
