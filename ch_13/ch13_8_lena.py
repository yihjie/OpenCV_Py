import cv2

src = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
dstx = cv2.Scharr(src, cv2.CV_32F, 1, 0)
dsty = cv2.Scharr(src, cv2.CV_32F, 0, 1)
dst_abs_x = cv2.convertScaleAbs(dstx)
dst_abs_y = cv2.convertScaleAbs(dsty)
dst = cv2.addWeighted(dst_abs_x,0.5, dst_abs_y,0.5, 0)

dstx_b = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dsty_b = cv2.Sobel(src, cv2.CV_32F, 0, 1)
dst_abs_x_b = cv2.convertScaleAbs(dstx_b)
dst_abs_y_b = cv2.convertScaleAbs(dsty_b)
dst_b = cv2.addWeighted(dst_abs_x_b,0.5, dst_abs_y_b,0.5, 0)



cv2.imshow('Src', src)
cv2.imshow('Scharr Dstx', dst_abs_x)
cv2.imshow('Scharr Dsty', dst_abs_y)
cv2.imshow("Scharr Dst", dst)
cv2.imshow("Sobel Dst", dst_b)

cv2.waitKey(0)
cv2.destroyAllWindows()
