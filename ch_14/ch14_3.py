# 向上採樣 pyrUp()

import cv2

src = cv2.imread('macau_small.jpg')
src_orig = cv2.imread('macau.jpg')
dst1 = cv2.pyrUp(src)
dst2 = cv2.pyrUp(dst1)
dst3 = cv2.pyrUp(dst2)

cv2.imshow('Level 0 - src', src)
cv2.imshow('Level 1 - dst1', dst1)
cv2.imshow('Level 2 - dst2', dst2)
cv2.imshow('Level 3 - dst3', dst3)
cv2.imshow('Origin', src_orig)

print(f"src.shape = {src.shape}")
print(f"dst1.shape = {dst1.shape}")
print(f"dst2.shape = {dst2.shape}")
print(f"dst3.shape = {dst3.shape}")
print(f"src_orig.shape = {src_orig.shape}")

cv2.waitKey(0)
cv2.destroyAllWindows()
