# Laplacian Pyramid, LP

import cv2
import numpy as np

src = np.random.randint(256, size=(4, 4), dtype=np.uint8)

G0 = src
G1 = cv2.pyrDown(src)
L0 = G0 - cv2.pyrUp(G1)
dst = L0 + cv2.pyrUp(G1)

print(f"G0=\n{G0}")
print(f"G1=\n{G1}")
print(f"L0=\n{L0}")
print(f"dst=\n{dst}")
