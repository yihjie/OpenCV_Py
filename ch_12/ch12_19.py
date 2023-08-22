# blackhat
# blackhat = src - close
# blackhat = src - erode(dilate())

import cv2
import numpy as np

kernel3 = np.ones((3, 3), np.uint8)
kernel5 = np.ones((5, 5), np.uint8)
kernel11 = np.ones((11, 11), np.uint8)

src = cv2.imread('snowman.jpg')
dst_3b = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel3)
dst_3c = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel3)
dst_3d = cv2.dilate(src, kernel3)
dst_3ed = cv2.erode(dst_3d, kernel3)
dst_3cs = dst_3c - src
dst_3eds = dst_3ed - src

dst_5b = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel5)
dst_5c = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel5)
dst_5d = cv2.dilate(src, kernel5)
dst_5ed = cv2.erode(dst_5d, kernel5)
dst_5cs = dst_5c - src
dst_5eds = dst_5ed - src

dst_11b = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel11)

cv2.imshow('Src', src)
cv2.imshow('Black Hat : Dst 3x3', dst_3b)
cv2.imshow('Closing 3x3 - Src', dst_3cs)
cv2.imshow('Erode(Dilate()) - Src', dst_3eds)
cv2.imshow('Black Hat : Dst 5x5', dst_5b)
cv2.imshow('Black Hat : Dst 11x11', dst_11b)

cv2.waitKey(0)
cv2.destroyAllWindows()
