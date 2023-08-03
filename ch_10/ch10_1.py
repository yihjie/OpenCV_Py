# cv2.resize()
# dsize

import cv2

src = cv2.imread('southpole.jpg')

width  = 300
height = 200
dsize = (width, height)

cut_src = src[0:200, 0:300, :]
dst = cv2.resize(src, dsize)

cv2.imshow("Src", src)
cv2.imshow("Dst", dst)
cv2.imshow("Cut-Src", cut_src)

cv2.waitKey(0)
cv2.destroyAllWindows()
