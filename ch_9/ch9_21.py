# cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
'''
adaptiveMethod : cv2.ADAPTIVE_THRESH_MEAN_C ; cv2.ADAPTIVE_THRESH_GAUSSIAN_C
thresholdType : cv2.THRESH_BINARY ; cv2.THRESH_BINARY_INV
'''

import cv2

thresh = 127
maxval = 255

src = cv2.imread('school.jpg', cv2.IMREAD_GRAYSCALE)

ret_b, dst_b = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
ret_o, dst_o = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
dst_mean = cv2.adaptiveThreshold(src, maxval, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
dst_gauss = cv2.adaptiveThreshold(src, maxval, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5)

cv2.imshow('Original image', src)
cv2.imshow('Threshold Binary', dst_b)
cv2.imshow('Threshold Binary - OTSU', dst_o)
cv2.imshow('Adaptive Mean C', dst_mean)
cv2.imshow('Adaptive Gaussian C', dst_gauss)

print(f"BINARY threshold = {ret_b}")
print(f"OTSU threshold = {ret_o}")

cv2.waitKey(0)
cv2.destroyAllWindows()
