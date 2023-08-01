# cv2.THRESH_BINARY + cv2.THRESH_OTSU

import cv2
import numpy as np

thresh_b = 127
thresh_o =   0
maxval   = 255

src = np.ones([3, 4], dtype=np.uint8) * 120
src[0:2, 0:2] = 108
'''
[
108, 108, 120, 120
108, 108, 120, 120
120, 120, 120, 120
120, 120, 120, 120
]
'''

ret_b, dst_b = cv2.threshold(src, thresh_b, maxval, cv2.THRESH_BINARY)
ret_o, dst_o = cv2.threshold(src, thresh_o, maxval, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

print(f"Binary threshold = {ret_b}")
print(f"src =\n{src}")
print(f"Binary dst =\n{dst_b}")
print('-' * 80)
print(f"OTSU threshold = {ret_o}")
print(f"src =\n{src}")
print(f"OTSU dst =\n{dst_o}")


