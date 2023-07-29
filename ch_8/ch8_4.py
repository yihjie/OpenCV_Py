# Modified from ch8_1.py
# 影像的加法運算
# res = cv2.add(src1, src2, dst=None, mask=None, dtype=None)

import cv2
import numpy as np

src1 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
src2 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
res  = src1 + src2

print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"res  = \n {res}")
