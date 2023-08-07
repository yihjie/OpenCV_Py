# Modified from ch10_4.py

# dst  = cv2.warpAffine(src, M ,dsize, flags, borderMode, borderValue)
# 影像平移

import cv2
import numpy as np

src = cv2.imread('rural.jpg')

height, width = src.shape[0:2]
dsize = (width, height)

# 平移 pixel
x = -50
y = -100

M = np.float32(([[1, 0 ,x],
                 [0, 1, y]]))

dst = cv2.warpAffine(src, M, dsize)

cv2.imshow("Src", src)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
