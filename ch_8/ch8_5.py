# Modified from ch8_2.py
# 灰階影像加成

import cv2
import numpy as np

img = cv2.imread('jk.jpg', cv2.IMREAD_GRAYSCALE)
img_gray = img.copy()
res1 = cv2.add(img, img)
res2 = img + img        # 超過 255 會轉成 256 的餘數，反而變黑
res3 = cv2.add(img_gray, img_gray)

cv2.imshow("Original Image", img)
cv2.imshow("Added Image2", res1)
cv2.imshow("Added Image3", res2)
cv2.imshow("Added Image4", res3)

cv2.waitKey(0)
cv2.destroyAllWindows()
