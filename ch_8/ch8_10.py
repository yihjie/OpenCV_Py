import cv2
import numpy as np

alpha = 1
beta  = 0.2
gamma = 1

src1 = cv2.imread('lake.jpg')
src2 = cv2.imread('geneva.jpg')
dst = cv2.addWeighted(src1, alpha, src2, beta, gamma)

cv2.imshow("Lake", src1)
cv2.imshow("Geneva", src2)
cv2.imshow("Lake + Geneva", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
