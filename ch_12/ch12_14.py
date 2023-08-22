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

kernel9= np.ones((9, 9), np.uint8)

src = cv2.imread('night.jpg')

dst_9c = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel9)
dst_9d = cv2.dilate(src, kernel9)
dst_9e = cv2.erode(dst_9d, kernel9)

cv2.imshow('Src', src)
cv2.imshow('Close - Dst 9 x 9', dst_9c)
cv2.imshow('Dilate - Dst 9 x 9', dst_9d)
cv2.imshow('Erode - Dst 9 x 9', dst_9e)

cv2.waitKey(0)
cv2.destroyAllWindows()
