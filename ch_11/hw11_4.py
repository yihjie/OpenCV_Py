# Modified from ch11_7.py

# 雙邊濾波器 vs 均值濾波器 vs 高斯濾波器
import cv2

src = cv2.imread('unistar.jpg')

dst1b = cv2.blur(src, (9, 9))
dst1g = cv2.GaussianBlur(src, (9, 9), 0, 0)
dst1bl = cv2.bilateralFilter(src, 9, 100, 100)

cv2.imshow('Src', src)
cv2.imshow('Blur - dst 9x9', dst1b)
cv2.imshow('Gaussian dst 9x9', dst1g)
cv2.imshow('Bilateral dst 9x9', dst1bl)

cv2.waitKey(0)
cv2.destroyAllWindows()
