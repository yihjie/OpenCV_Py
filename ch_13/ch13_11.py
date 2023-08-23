import cv2

# 1. 使用 cv2.IMREAD_GRAYSCALE 取得灰階影像
# 2. 使用 cv2.GaussianBlur() 降噪
src = cv2.imread('geneva.jpg', cv2.IMREAD_GRAYSCALE)
#src = cv2.imread('geneva.jpg')
src = cv2.GaussianBlur(src, (3, 3), 0)

# Sobel()
dstx_b = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dsty_b = cv2.Sobel(src, cv2.CV_32F, 0, 1)
dstx_b_abs = cv2.convertScaleAbs(dstx_b)
dsty_b_abs = cv2.convertScaleAbs(dsty_b)
dst_b = cv2.addWeighted(dstx_b_abs, 0.5, dsty_b_abs, 0.5, 0)

# Scharr()
dstx_c = cv2.Scharr(src, cv2.CV_32F, 1, 0)
dsty_c = cv2.Scharr(src, cv2.CV_32F, 0, 1)
dstx_c_abs = cv2.convertScaleAbs(dstx_c)
dsty_c_abs = cv2.convertScaleAbs(dsty_c)
dst_c = cv2.addWeighted(dstx_c_abs, 0.5, dsty_c_abs, 0.5, 0)

# Laplacian()
dst_l = cv2.Laplacian(src, cv2.CV_32F, ksize=3)
dst_l_abs =  cv2.convertScaleAbs(dst_l)

cv2.imshow('Src', src)
cv2.imshow('Sobel - Dst', dst_b)
cv2.imshow('Scharr - Dst', dst_c)
cv2.imshow('Laplacian - Dst', dst_l_abs)

cv2.waitKey(0)
cv2.destroyAllWindows()
