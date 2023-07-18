# 1. Create 5x12 Gray array
# 2. print the pixel of [1,3] and modify it to 255
# 3. display these two array

import cv2
import numpy as np

image = np.zeros((5, 12), np.uint8)
image_clone = image.copy()
image[1, 4] = 255

print(f"修改前 image = \n{image_clone}")
print(f"修改前 image[1, 4] = {image_clone[1, 4]}")
print("-" * 70)

print(f"修改後 image = \n{image}")
print(f"修改後 image[1, 4] = {image[1,4]}")
