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
image[:, :, 0] = 255  # Blue

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
