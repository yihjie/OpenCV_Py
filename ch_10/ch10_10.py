# 透視圖
# M = cv2.getPerspectiveTransform ( src_p, dst_p )
# dst = cv2.wrapPerspective(src, M ,dsize, flags, borderMode, borderValue)

import cv2
import numpy as np

src = cv2.imread('tunnel.jpg')

height, width = src.shape[:2]
dsize = (width, height)

src_p = np.float32([[0, 0],
                    [width, 0],
                    [0, height],
                    [width - 1, height - 1]])

dst_p = np.float32([[150, 0],
                    [width - 150, 0],
                    [0, height - 1],
                    [width - 1, height - 1]])

M = cv2.getPerspectiveTransform(src_p, dst_p)

dst = cv2.warpPerspective(src, M, dsize)

cv2.imshow("Src", src)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
