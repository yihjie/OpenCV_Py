# Custom Kernel
# cv2.getStructuringElement(shape, ksize, anchor)
'''
shape :
    1. MORPH_RECT           : 所有元素都是 1
    2. MORPH_ELLIPSE        : 橢圓形結構 1
    3. MORPH_CROSS          : 十字形位置 1
'''

import cv2

kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
kernel_cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

print("MORPH_RECT")
print(kernel_rect)
print("MORPH_ELLIPSE")
print(kernel_ellipse)
print("MORPH_CROSS")
print(kernel_cross)
