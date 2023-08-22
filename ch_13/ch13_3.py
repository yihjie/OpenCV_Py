# 計算 dx , 所以 dy = 0
# dst = cv2.Sobel(src ,ddepth, 1, 0)

import cv2

src = cv2.imread('map.jpg')
dst_x = cv2.Sobel(src, cv2.CV_32F,1, 0)
dst_y = cv2.Sobel(src, cv2.CV_32F, 0, 1)
dst_mx = cv2.convertScaleAbs(dst_x)
dst_my = cv2.convertScaleAbs(dst_y)
dst = cv2.addWeighted(dst_mx, 0.5, dst_my, 0.5, 0)

cv2.imshow('Src', src)
cv2.imshow('dx(src)', dst_x)
cv2.imshow('dy(src)', dst_y)
cv2.imshow('Modified dx(src)', dst_mx)
cv2.imshow('Modified dy(src)', dst_my)
cv2.imshow('Combined', dst)


cv2.waitKey(0)
cv2.destroyAllWindows()
