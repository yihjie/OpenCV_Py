# 灰階影像加成

import cv2
import numpy as np

img = cv2.imread('jk.jpg', cv2.IMREAD_GRAYSCALE)
res = cv2.add(img, img)

cv2.imshow("Original Image", img)
cv2.imshow("Added Image", res)

cv2.waitKey(0)
cv2.destroyAllWindows()
