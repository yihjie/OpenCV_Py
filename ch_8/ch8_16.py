# cv2.bitwise_not(src, mask=None)

import cv2
import numpy as np

src = cv2.imread('forest.jpg')
dst = cv2.bitwise_not(src)

cv2.imshow("Origin - forest", src)
cv2.imshow("Not - forest", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
