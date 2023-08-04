# M = cv2.getAffineTransform(src_p, dst_p)
# dst = cv2.warpAffine(src, M, dsize)
# src([0,0], [width - 1, 0], [0, height - 1])
# dst([0,0],[width - 1 - 30, 0], [30, height - 1])


import cv2
import numpy as np

src = cv2.imread('rural.jpg')
height, width = src.shape[0:2]
dsize = (width, height)

src_p = np.float32([[0, 0],
                    [width - 1, 0],
                    [0, height - 1]])

dst_p = np.float32([[0, 0],
                    [width -1 - 30, 0],
                    [30, height - 1]])

M = cv2.getAffineTransform(src_p, dst_p)

dst = cv2.warpAffine(src, M, dsize)

cv2.imshow("Src", src)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
