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

kernel9 = np.ones((9, 9), np.uint8)

src = cv2.imread('night.jpg')

dst9 = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel9)

cv2.imshow('Src', src)
cv2.imshow('Open - Dst 9x9', dst9)

cv2.waitKey(0)
cv2.destroyAllWindows()
