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

kernel11 = np.ones((11, 11), np.uint8)

src = cv2.imread('snowman.jpg')
src1 = cv2.imread('snowman1.jpg')

dst_11c = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel11)
dst_11o = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel11)
dst_11c1 = cv2.morphologyEx(src1, cv2.MORPH_CLOSE, kernel11)
dst_11o1 = cv2.morphologyEx(src1, cv2.MORPH_OPEN, kernel11)


cv2.imshow('Src - snowman', src)
cv2.imshow('Close - snowman - Dst 11x11', dst_11c)
cv2.imshow('Open - snowman - Dst 11x11', dst_11o)
cv2.imshow('Src - snowman1', src1)
cv2.imshow('Close - snowman1 - Dst 11x11', dst_11c1)
cv2.imshow('Open - snowman1 - Dst 11x11', dst_11o1)


cv2.waitKey(0)
cv2.destroyAllWindows()
