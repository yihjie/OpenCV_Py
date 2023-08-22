# MorphologyEx
# dst = cv2.morphologyeEx(src, op, kernel, anchor, iteration, borderType, borderValue)
'''
op :
    MORPH_ERODE     = erode()
    MORPH_DILATE    = dilate()
    MORPH_OPEN      = dilate(erode())
    MORPH_CLOSE     = erode(dilate())
    MORPH_GRADIENT  = dilate() - erode()
    MORPH_TOPHAT    = src - open()
    MORPH_BLACKHAT  = close() - src
    MORPH_HITMISS   = intersection(erode(src), erode(src1))
'''

import cv2
import numpy as np

kernel5 = np.ones((5, 5), np.uint8)

src = cv2.imread('k.jpg')
dst_5d = cv2.dilate(src, kernel5)
dst_5e = cv2.erode(src, kernel5)
dst_5g = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, kernel5)
dst_5de = dst_5d - dst_5e

cv2.imshow('Src', src)
cv2.imshow('Gradient - Dst 5x5', dst_5g)
cv2.imshow('Dilate - Dst 5x5', dst_5d)
cv2.imshow('Erode - Dst 5x5', dst_5e)
cv2.imshow('Dilate - Erode - Dst 5x5', dst_5de)

cv2.waitKey(0)
cv2.destroyAllWindows()
