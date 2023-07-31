# modify the mask from ch8_13.py
import cv2
import numpy as np

src1 = cv2.imread('geneva.jpg')
mask = np.zeros(src1.shape, dtype=np.uint8)
mask_copy = mask.copy()

ly1 = int(src1.shape[1] / 3) - 1
ly2 = int(src1.shape[1] / 3 * 2) - 1
rx1 = int(src1.shape[0] / 3) - 1
rx2 = int(src1.shape[0] / 3 * 2) - 1

mask[:, ly1:ly2, :] = 255
mask[rx1:rx2, :, :] = 255

dst  = cv2.bitwise_and(src1, mask)

cv2.imshow("src1 - geneva", src1)
cv2.imshow("Mask", mask)
cv2.imshow("Result - dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
