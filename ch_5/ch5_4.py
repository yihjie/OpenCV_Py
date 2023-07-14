import cv2
import numpy as np

height_size = 160
width_size = 280

white_height_top = 40
white_height_bottom = 120
white_width_left = 70
white_width_right = 210

image = np.zeros((height_size, width_size), np.uint8)  # 黑色
image[white_height_top:white_height_bottom, white_width_left:white_width_right] = 255  # 白色

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
