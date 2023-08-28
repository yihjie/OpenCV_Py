# 向下採樣 pyrDown()

import cv2

src = cv2.imread('macau.jpg')
dst1 = cv2.pyrDown(src)
dst2 = cv2.pyrDown(dst1)
dst3 = cv2.pyrDown(dst2)

cv2.imshow('Level 0 - src', src)
cv2.imshow('Level 1 - dst1', dst1)
cv2.imshow('Level 2 - dst2', dst2)
cv2.imshow('Level 3 - dst3', dst3)


print(f"src.shape = {src.shape}")
print(f"dst1.shape = {dst1.shape}")
print(f"dst2.shape = {dst2.shape}")
print(f"dst3.shape = {dst3.shape}")

cv2.waitKey(0)
cv2.destroyAllWindows()
