# 垂直翻轉
'''
使用 remap()
map1 (mapX) : 不變
map2 (mapY) : rows - 1 - r
'''

import cv2
import numpy as np

src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)

rows, cols = src.shape
mapX = np.zeros(src.shape, np.float32)
mapY = np.zeros(src.shape, np.float32)

for r in range(rows):
    for c in range(cols):
        mapX.itemset((r, c), c)
        mapY.itemset((r, c), rows - 1 - r)  # 垂直鏡射

dst = cv2.remap(src, mapX, mapY, cv2.INTER_LINEAR)

print(f"src =\n{src}")
print(f"dst =\n{dst}")
print('-' * 80)
print(f"mapX =\n{mapX}")
print(f"mapY =\n{mapY}")
