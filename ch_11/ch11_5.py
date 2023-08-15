# 高斯濾波器
# dst = cv2.GaussianBlur(src, ksize, sigmaX, sigmaY, borderType)

import cv2

src = cv2.imread('hung.jpg')

dst1 = cv2.GaussianBlur(src, (3, 3), 0, 0)
dst2 = cv2.GaussianBlur(src, (5, 5), 0, 0)
dst3 = cv2.GaussianBlur(src, (29, 29), 0, 0)

cv2.imshow('Src' , src)
cv2.imshow('Dst 3x3', dst1)
cv2.imshow('Dst 5x5', dst2)
cv2.imshow('Dst 29x29', dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()
