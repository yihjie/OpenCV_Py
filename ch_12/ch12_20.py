# blackhat
# blackhat = src - close
# blackhat = src - erode(dilate())

import cv2
import numpy as np

kernel11 = np.ones((11, 11), np.uint8)

src = cv2.imread('excel.jpg')
dst_11b = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel11)

cv2.imshow('Src', src)
cv2.imshow('Black Hat : Dst 11x11', dst_11b)

cv2.waitKey(0)
cv2.destroyAllWindows()
