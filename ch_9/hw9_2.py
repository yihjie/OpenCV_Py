# Modified from ch9_8.py
# number recognization

import cv2

src = cv2.imread('number.jpg')

thresh = 1
maxval = 255

ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)

cv2.imshow('Src', src)
cv2.imshow(f"INV DST-{ret}", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
