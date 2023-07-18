# draw ch6_3.py
# resize the array from 2x3 to 100x150

# 1. create 3 array 2x3 to split blue, green, and red
# 2. print the contents of these arraies

import cv2
import numpy as np

height = 100
width  = 150
# create blue channel
blue_img = np.zeros((height, width, 3), np.uint8)
blue_img[:, :, 0] = 255

# create green channel
green_img = np.zeros((height, width, 3), np.uint8)
green_img[:, :, 1] = 255

# create red channel
red_img = np.zeros((height, width, 3), np.uint8)
red_img[:, :, 2] = 255

# draw the image
cv2.imshow("blue image", blue_img)
cv2.imshow("green image", green_img)
cv2.imshow("red image", red_img)

# close all image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
