# 中值濾波器
# dst = cv2.medianBlur(src, ksize)

import cv2
import numpy as np

src = np.ones((3, 3), np.float32) * 150
src[1,1] = 20
dst = cv2.medianBlur(src, 3)

print(f"src =\n{src}")
print(f"dst =\n{dst}")
