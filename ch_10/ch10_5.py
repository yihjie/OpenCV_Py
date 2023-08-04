# M = cv2.getRotationMatrix2D(center, angle, scale)

import cv2

src = cv2.imread('rural.jpg')

height, width = src.shape[0:2]
dsize = (width, height)

M1 = cv2.getRotationMatrix2D((width/2, height/2), 30, 1)  # 逆時鐘
M2 = cv2.getRotationMatrix2D((width/2, height/2), -30, 1)       # 順時鐘

dst1 = cv2.warpAffine(src, M1, dsize)
dst2 = cv2.warpAffine(src, M2, dsize)

cv2.imshow("Src", src)
cv2.imshow("Dst - 30", dst1)
cv2.imshow("Dst - -30", dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()
