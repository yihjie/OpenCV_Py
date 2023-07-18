# modified one pixel
import cv2
import numpy as np

blue = np.zeros((2, 3, 3), np.uint8)
blue[:, :, 0] = 255

print(f"blue = \n {blue}")
print(f"blue[0, 1, 2] before modified = {blue[0, 1, 2]}")

blue[0, 1, 2] = 50

print(f"blue[0, 1, 2] after modified = {blue[0, 1, 2]}")
print(f"blue = \n {blue}")
