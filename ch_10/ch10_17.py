# 影像縮放
# 縮小 0.25
'''
mapX = 2 * ( c - cols * 0.25 )
mapY = 2 * ( r - rows * 0.25 )
'''

import cv2
import numpy as np

src = cv2.imread('tunnel.jpg')

rows, cols = src.shape[:2]
mapX = np.zeros(src.shape[:2], np.float32)
mapY = np.zeros(src.shape[:2], np.float32)

for r in range(rows):
    for c in range(cols):
        if (0.25 * rows < r < 0.75 * rows) and (0.25 * cols < c < 0.75 * cols):
            mapX.itemset((r, c), 2 *( c - cols * 0.25))
            mapY.itemset((r, c), 2 * (r - rows * 0.25))
        else:
            mapX.itemset((r, c), 0)
            mapY.itemset((r, c), 0)

dst = cv2.remap(src, mapX, mapY, cv2.INTER_LINEAR)

cv2.imshow('Src', src)
cv2.imshow('Dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
