# THRESH_BINARY_INV

import cv2
import numpy as np

thresh = 127
maxval = 255

src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
ret, dst  =cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)

print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst = \n {dst}")
