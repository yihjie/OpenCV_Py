# 計算 dx , 所以 dy = 0
# dst = cv2.Sobel(src ,ddepth, 1, 0)

import cv2

src = cv2.imread('map.jpg')
dst_x = cv2.Sobel(src, -1,1, 0)
dst_y = cv2.Sobel(src, -1, 0, 1)

cv2.imshow('Src', src)
cv2.imshow('dx(src)', dst_x)
cv2.imshow('dy(src)', dst_y)

cv2.waitKey(0)
cv2.destroyAllWindows()
