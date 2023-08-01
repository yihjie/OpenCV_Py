# number recognization

import cv2

src = cv2.imread('number.jpg')

thresh_1 = 127
thresh_2 = 10
maxval = 255

ret1, dst1 = cv2.threshold(src, thresh_1, maxval, cv2.THRESH_BINARY)
ret2, dst2 = cv2.threshold(src, thresh_2, maxval, cv2.THRESH_BINARY)

cv2.imshow('Src', src)
cv2.imshow('DST-127', dst1)
cv2.imshow('DST - 10', dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()
