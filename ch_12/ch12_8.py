# Dilate()
# kernel = 3x3 , 5x5

import cv2
import numpy as np

src = cv2.imread('whilster.jpg')

kernel3 = np.ones((3, 3), np.uint8)
kernel5 = np.ones((5, 5), np.uint8)

dst3e = cv2.erode(src, kernel3)
dst5e = cv2.erode(src, kernel5)

dst3d = cv2.dilate(src, kernel3)
dst5d = cv2.dilate(src, kernel5)

cv2.imshow('Src', src)
cv2.imshow('Erosion 3x3', dst3e)
cv2.imshow('Erosion 5x5', dst5e)
cv2.imshow('Dilate 3x3', dst3d)
cv2.imshow('Dilate 5x5', dst5d)

cv2.waitKey(0)
cv2.destroyAllWindows()
