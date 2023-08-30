# Modified from ch15_1.py
import cv2
import numpy as np

src = cv2.imread('lake.jpg')
src_copy = src.copy()
# 1.
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 2.
ret, dst_binary = cv2.threshold(src_gray, 150, 255, cv2.THRESH_BINARY)
# 3.
contours, hierarchy = cv2.findContours(dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# 4.
mask = np.zeros(src.shape, np.int8)
dst = cv2.drawContours(mask, contours, -1, (255, 255,255), -1)
dst_result = np.bitwise_and(src, mask)


cv2.imshow('Src', src_copy)
cv2.imshow('Src Binary', dst_binary)
cv2.imshow('RST', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
