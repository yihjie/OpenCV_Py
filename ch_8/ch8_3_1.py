# 彩色影像加成, 亮度微調

import cv2
import numpy as np

value = 20 # 亮度

img = cv2.imread('jk.jpg')
coff = np.ones(img.shape, dtype=np.uint8) * value
res = cv2.add(img, coff)

cv2.imshow("Original Image", img)
cv2.imshow("Added Image", res)

cv2.waitKey(0)
cv2.destroyAllWindows()
