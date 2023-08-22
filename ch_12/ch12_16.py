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

kernel3 = np.ones((3,3), np.uint8)

src = cv2.imread('hole.jpg')
dst_3g = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, kernel3)

cv2.imshow('Src', src)
cv2.imshow('Gradient - Dst 3x3', dst_3g)

cv2.waitKey(0)
cv2.destroyAllWindows()
