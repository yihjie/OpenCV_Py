# OpenCV add Weighted
# dst = saturate(src1 * alpha + src2 * beta + gamma )
# dst = cv2.addWeighted(src1, alpha, src2, beta, gamma)

import cv2
import numpy as np

src1 = np.ones((2, 3), dtype=np.uint8) * 10
src2 = np.ones((2, 3), dtype=np.uint8) * 50

alpha = 1
beta  = 0.5
gamma = 5

dst = cv2.addWeighted(src1, alpha, src2, beta, gamma)

print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"dst = \n {dst}")

print(f"result = \n {(src1 * alpha + src2 * beta + gamma).astype(int)}")