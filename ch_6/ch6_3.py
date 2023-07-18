# 1. create 3 array 2x3 to split blue, green, and red
# 2. print the contents of these arraies

import cv2
import numpy as np

height = 2
width  = 3

# create blue channel
blue_img = np.zeros((height, width, 3), np.uint8)
blue_img[:, :, 0] = 255

# create green channel
green_img = np.zeros((height, width, 3), np.uint8)
green_img[:, :, 1] = 255

# create red channel
red_img = np.zeros((height, width, 3), np.uint8)
red_img[:, :, 2] = 255

# print the contents
print(f"blue image = \n{blue_img}")
print("-" * 70)
print(f"green image = \n{green_img}")
print("-" * 70)
print(f"red image = \n{red_img}")
