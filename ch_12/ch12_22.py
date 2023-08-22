# Custom Kernel
# cv2.getStructuringElement(shape, ksize, anchor)
'''
shape :
    1. MORPH_RECT           : 所有元素都是 1
    2. MORPH_ELLIPSE        : 橢圓形結構 1
    3. MORPH_CROSS          : 十字形位置 1
'''

import cv2

kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (39, 39))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (39, 39))
kernel_cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (39, 39))

src = cv2.imread('bw_circle.jpg')
dst_rect = cv2.dilate(src, kernel_rect)
dst_ellipse = cv2.dilate(src, kernel_ellipse)
dst_cross = cv2.dilate(src, kernel_cross)

cv2.imshow('Src', src)
cv2.imshow('MORPH Rect', dst_rect)
cv2.imshow('MORPH Ellipse', dst_ellipse)
cv2.imshow('MORPH Cross', dst_cross)

cv2.waitKey(0)
cv2.destroyAllWindows()
