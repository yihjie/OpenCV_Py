# 建立黑白相間的影像

import cv2
import numpy as np

height = 160
width = 280

image = np.zeros((height, width), np.uint8)
for y in range(0, height, 20):  # 每隔 20px 進行切換
    image[y:y + 10, :] = 255  # 白色帶寬 10

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
