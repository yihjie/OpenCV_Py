# 中值濾波器
# dst = cv2.medianBlur(src, ksize)
import cv2

src = cv2.imread('hung.jpg')

dst1 = cv2.medianBlur(src, 3)
dst2 = cv2.medianBlur(src, 5)
dst3 = cv2.medianBlur(src, 7)

cv2.imshow('Src', src)
cv2.imshow('Dst 3x3', dst1)
cv2.imshow('Dst 5x5', dst2)
cv2.imshow('Dst 7x7', dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()
