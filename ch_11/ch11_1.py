# 均值濾波器函數
# dst = cv2.blur(src, ksize, anchor, borderType)

import cv2

src = cv2.imread('hung.jpg')

dst1 = cv2.blur(src, (3, 3))
dst2 = cv2.blur(src, (5, 5))
dst3 = cv2.blur(src, (7, 7))
dst29 = cv2.blur(src, (29, 29))


cv2.imshow('Src', src)
cv2.imshow('Dst - 3x3', dst1)
cv2.imshow('Dst - 5x5', dst2)
cv2.imshow('Dst - 7x7', dst3)
cv2.imshow('Dst - 29x29', dst29)

cv2.waitKey(0)
cv2.destroyAllWindows()
