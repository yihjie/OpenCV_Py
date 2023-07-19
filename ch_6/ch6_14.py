# 對 ROI 建立馬賽克

import cv2
import numpy as np

img = cv2.imread('jk.jpg')
img_clone = img.copy()

face = np.random.randint(0, 256, size=(190, 170, 3)) # 馬賽克
img[30:220, 80:250] = face

cv2.imshow("Hung Image", img_clone)
cv2.imshow("Face", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
