# 隨機灰階影像
import cv2
import numpy as np

height = 160
width = 280

image = np.random.randint(256, size=[height, width], dtype=np.uint8)

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
