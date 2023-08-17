# Dilate()
# kernel = 3x3 , 5x5

import cv2
import numpy as np

src = cv2.imread('a.jpg')

kernel3 = np.ones((3, 3), np.uint8)
kernel5 = np.ones((5, 5), np.uint8)

dst3 = cv2.dilate(src, kernel3)
dst5 = cv2.dilate(src, kernel5)

cv2.imshow('Src', src)
cv2.imshow('Dilate 3x3', dst3)
cv2.imshow('Dilate 5x5', dst5)

cv2.waitKey(0)
cv2.destroyAllWindows()
