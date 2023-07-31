import cv2
import numpy as np

src1 = cv2.imread('jk.jpg', cv2.IMREAD_GRAYSCALE)
src2 = np.zeros(src1.shape, dtype=np.uint8)
src2[30:260, 70:260] = 255

dst  = cv2.bitwise_and(src1, src2)

cv2.imshow("src1 - jk", src1)
cv2.imshow("Mask - src2", src2)
cv2.imshow("Result - dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
