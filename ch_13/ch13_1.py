# cv2.convertScaleAbs()

import cv2
import numpy as np

src = np.random.randint(-256, 256, size=[3, 5], dtype=np.int16)
dst = cv2.convertScaleAbs(src)

print("src = ")
print(src)
print('-' * 80)
print("Abs(src) = ")
print(dst)
