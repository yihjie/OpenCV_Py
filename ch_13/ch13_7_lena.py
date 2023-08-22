import cv2

src = cv2.imread('lena.jpg')
dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)
dst_abs_x = cv2.convertScaleAbs(dstx)
dst_abs_y = cv2.convertScaleAbs(dsty)
dst = cv2.addWeighted(dst_abs_x,0.5, dst_abs_y,0.5, 0)

cv2.imshow('Src', src)
cv2.imshow('Dstx', dst_abs_x)
cv2.imshow('Dsty', dst_abs_y)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
