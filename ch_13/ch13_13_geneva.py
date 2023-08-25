import cv2

src = cv2.imread('geneva.jpg', cv2.IMREAD_GRAYSCALE)

# 1. 降低噪音
src = cv2.GaussianBlur(src, (3, 3), 0)

# Sobel()
dst_x_s = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dst_y_s = cv2.Sobel(src, cv2.CV_32F, 0 , 1)
dst_x_s = cv2.convertScaleAbs(dst_x_s)
dst_y_s = cv2.convertScaleAbs(dst_y_s)
dst_s = cv2.addWeighted(dst_x_s, 0.5, dst_y_s, 0.5, 0)

# Scharr()
dst_x_r = cv2.Scharr(src, cv2.CV_32F, 1, 0)
dst_y_r = cv2.Scharr(src, cv2.CV_32F, 0, 1)
dst_x_r = cv2.convertScaleAbs(dst_x_r)
dst_y_r = cv2.convertScaleAbs(dst_y_r)
dst_r = cv2.addWeighted(dst_x_r, 0.5, dst_y_r, 0.5, 0)

# Laplacian()
dst_l = cv2.Laplacian(src, cv2.CV_32F, ksize=3)
dst_l = cv2.convertScaleAbs(dst_l)

# Canny()
dst_c = cv2.Canny(src, 50, 100)

cv2.imshow('Src', src)
cv2.imshow('Sobel()', dst_s)
cv2.imshow('Scharr()', dst_r)
cv2.imshow('Laplacian()', dst_l)
cv2.imshow('Canny()', dst_c)

cv2.waitKey(0)
cv2.destroyAllWindows()
