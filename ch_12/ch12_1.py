# Erosion
# dst = cv2.erode(src, kernel, anchor, iterations, borderType, borderValue)
# kernel = 3x3

import cv2
import numpy as np

src = np.zeros((7, 7), np.uint8)
src[1:6, 1:6] = 1

kernel = np.ones((3, 3), np.uint8)

dst = cv2.erode(src, kernel)

print(f"src =\n{src}")
print(f"kernel =\n{kernel}")
print(f"Erosion =\n{dst}")
