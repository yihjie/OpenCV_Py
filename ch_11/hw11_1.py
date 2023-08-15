# extened ch11_3.py

import cv2
import numpy as np

src = np.ones((5, 5), np.float32) * 150

for r in range(src.shape[0]):
    src[r,r] = 20

dst3 = cv2.medianBlur(src, 3)
dst5 = cv2.medianBlur(src, 5)

print(f"src =\n{src}")
print(f"dst 3 =\n{dst3}")
print(f"dst 5 =\n{dst5}")
