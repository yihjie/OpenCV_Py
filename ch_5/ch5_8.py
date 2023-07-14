# 建立 BGR 彩色影像
#
# index[:, :, 0] -- Blue
# index[:, :, 1] -- Green
# index[:, :, 2] -- Red

import cv2
import numpy as np

height = 160
width = 280

image = np.zeros((height, width, 3), np.uint8)

blue_image = image.copy()
blue_image[:, :, 0] = 255
green_image = image.copy()
green_image[:, :, 1] = 255
red_image = image.copy()
red_image[:, :, 2] = 255

cv2.imshow("Origin Image", image)
cv2.imshow("Blue", blue_image)
cv2.imshow("Green", green_image)
cv2.imshow("Red", red_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
