# modified from ch6_6.py

import cv2
import numpy as np

blue = np.zeros((2, 3, 3), np.uint8)
blue[:, :, 0] = 255

print(f"blue = \n {blue}")
print(f"blue[0, 1, 2] before modified = {blue.item(0, 1, 2)}")  # blue[0, 1, 2] = blue.item(0, 1, 2)

#blue[0, 1, 2] = 50
blue.itemset((0, 1, 2), 50)

print(f"blue[0, 1, 2] after modified = {blue.item(0, 1, 2)}")   # blue[0, 1, 2] = blue.item(0, 1, 2)
print(f"blue = \n {blue}")
