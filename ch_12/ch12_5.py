# dilate()
# dst = cv2.dilate(src, kernel, anchor, iterations, borderType, borderValue)

import cv2
import numpy as np

src = np.zeros((7, 7), np.uint8)
src[2:5, 2:5] = 1

kernel = np.ones((3, 3), np.uint8)

dst = cv2.dilate(src, kernel)

print(f"src =\n{src}")
print(f"kernel =\n{kernel}")
print(f"dst =\n{dst}")
