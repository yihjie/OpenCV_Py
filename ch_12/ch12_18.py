# tophat
# cv2.MORPH_TOPHAT = src - cv2.MORPH_OPEN
# cv2.MORPH_TOPHAT = src - cv2.dilate(cv2.erode())

import cv2
import numpy as np

kernel3 = np.ones((3, 3), np.uint8)

src = cv2.imread('btree.jpg')

dst_3t = cv2.morphologyEx(src, cv2.MORPH_TOPHAT, kernel3)
dst_3o = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel3)
dst_3e = cv2.erode(src, kernel3)
dst_3de = cv2.dilate(dst_3e, kernel3)
dst_3so = src - dst_3o
dst_3sde = src - dst_3de

cv2.imshow('Src' , src)
cv2.imshow('Tophat Dst 3x3', dst_3t)
cv2.imshow('Open Dst 3x3', dst_3o)
cv2.imshow('Src - Open Dst 3x3', dst_3so)
cv2.imshow('Dilate(Erode()) - Dst 3x3', dst_3de)
cv2.imshow('Src - Dilate(Erode())', dst_3sde)

cv2.waitKey(0)
cv2.destroyAllWindows()
