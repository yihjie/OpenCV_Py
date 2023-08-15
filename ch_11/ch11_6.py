# 均值濾波器 vs 高斯濾波器
import cv2

src = cv2.imread('border.jpg')

# 均值濾波器
dst1b = cv2.blur(src, (3,3))
dst2b = cv2.blur(src, (7, 7))

# 高斯濾波器
dst1g = cv2.GaussianBlur(src, (3, 3), 0, 0)
dst2g = cv2.GaussianBlur(src, (7, 7), 0, 0)

cv2.imshow('Src', src)
cv2.imshow('Blur - Dst 3x3', dst1b)
cv2.imshow('Gaussian - Dst 3x3', dst1g)
cv2.imshow('Blur - Dst 7x7', dst2b)
cv2.imshow('Gaussian - Dst 7x7', dst2g)

cv2.waitKey(0)
cv2.destroyAllWindows()
