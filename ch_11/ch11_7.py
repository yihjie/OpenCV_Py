# 雙邊濾波器 vs 均值濾波器 vs 高斯濾波器
import cv2

src = cv2.imread('hung.jpg')

dst1b = cv2.blur(src, (15,15))
dst1g = cv2.GaussianBlur(src, (15, 15), 0, 0)
dst1bl = cv2.bilateralFilter(src, 15, 100, 100)

cv2.imshow('Src', src)
cv2.imshow('Blur - dst 15x15', dst1b)
cv2.imshow('Gaussian dst 15x15', dst1g)
cv2.imshow('Bilateral dst 15x15', dst1bl)

cv2.waitKey(0)
cv2.destroyAllWindows()
