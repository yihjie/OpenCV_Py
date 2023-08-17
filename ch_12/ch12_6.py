# dilate()
# dst = cv2.dilate(src, kernel, anchor, iterations, borderType, borderValue)
# kernel : 5x5 , 11x11

import cv2
import numpy as np

src = cv2.imread('bw_dilate.jpg')

kernel5 = np.ones((5, 5), np.uint8)
kernel11 = np.ones((11, 11), np.uint8)

dst5 = cv2.dilate(src, kernel5)
dst11 = cv2.dilate(src, kernel11)

cv2.imshow('Src', src)
cv2.imshow('Dilate 5x5', dst5)
cv2.imshow('Dilate 11x11', dst11)

cv2.waitKey(0)
cv2.destroyAllWindows()
