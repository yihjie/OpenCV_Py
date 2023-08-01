# cv2.THRESH_BINARY + cv2.THRESH_OTSU

import cv2
import numpy as np

thresh_b = 127
thresh_o = 127
maxval   = 255

src = np.ones([3, 4], dtype=np.uint8) * 150
src[0:2, 0:2] = 120
'''
[
108, 108, 120, 120
108, 108, 120, 120
120, 120, 120, 120
120, 120, 120, 120
]
'''

src_ran = np.random.randint(0, 256, size=[3, 4], dtype=np.uint8)


ret_b, dst_b = cv2.threshold(src_ran, thresh_b, maxval, cv2.THRESH_BINARY)
ret_o, dst_o = cv2.threshold(src_ran, thresh_o, maxval, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

print(f"Binary threshold = {ret_b}")
print(f"src =\n{src_ran}")
print(f"Binary dst =\n{dst_b}")
print('-' * 80)
print(f"OTSU threshold = {ret_o}")
print(f"src =\n{src_ran}")
print(f"OTSU dst =\n{dst_o}")


