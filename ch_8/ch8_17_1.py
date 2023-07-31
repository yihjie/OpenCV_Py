import cv2
import numpy as np

src1 = cv2.imread('forest.jpg')
src2 = np.zeros(src1.shape, np.uint8)
src2[:, 120:360, :] = 255
dst = cv2.bitwise_xor(src1, src2)

dst2 = cv2.bitwise_xor(dst, src2)

cv2.imshow("Origin - forest", src1)
cv2.imshow("Mask", src2)
cv2.imshow("Origin xor Mask", dst)

cv2.imshow("dst xor mask", dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()
