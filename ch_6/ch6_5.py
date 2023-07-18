import cv2
import numpy as np

blue = np.zeros((2, 3, 3), np.uint8)
blue[:, :, 0] = 255 # 0 - blue ; 1 - green ; 2 - red
print(f"blue = \n{blue}")
print(f"blue[0, 1] before modified - {blue[0, 1]}")

blue[0,1] = [50, 100, 150]
print(f"blue[0, 1] after modified = {blue[0, 1]}")
print(f"blue = \n{blue}")
