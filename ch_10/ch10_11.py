# 重映射 (remap)
# dst = cv2.remap(src, map1, map2, interpolation, borderMode, borderValue)

import cv2
import numpy as np

src = np.random.randint(0, 256, size=[3, 4], dtype=np.uint8)

rows, cols = src.shape

mapX = np.ones(src.shape, np.float32) * 2
mapY = np.ones(src.shape, np.float32) * 0

dst = cv2.remap(src, mapX, mapY, cv2.INTER_LINEAR)

print(f"src =\n {src}")
print(f"dst =\n {dst}")
print('-' * 80)
print(f"mapX = \n {mapX}")
print(f"mapY = \n {mapY}")
