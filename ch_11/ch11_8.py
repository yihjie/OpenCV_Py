# 自製濾波器
# dst = cv2.filter2D(src, ddepth, kernel, anchor, delta, borderType)

'''
k = (1/121)[11,11]
'''

import cv2
import numpy as np

kernel = np.ones((11, 11), np.float32) / 121

src = cv2.imread('hung.jpg')

dst = cv2.filter2D(src, -1, kernel)

cv2.imshow('Src', src)
cv2.imshow('Customer Filter - Dst 11x11', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
