import cv2

# 1. 使用 cv2.IMREAD_GRAYSCALE 取得灰階影像
# 2. 使用 cv2.GaussianBlur() 降噪
src = cv2.imread('geneva.jpg', cv2.IMREAD_GRAYSCALE)
#src = cv2.imread('geneva.jpg')
src = cv2.GaussianBlur(src, (3, 3), 0)


# Laplacian()
dst_l_1 = cv2.Laplacian(src, cv2.CV_32F, ksize=1)
dst_l_abs_1 =  cv2.convertScaleAbs(dst_l_1)

dst_l_3 = cv2.Laplacian(src, cv2.CV_32F, ksize=3)
dst_l_abs_3 =  cv2.convertScaleAbs(dst_l_3)

dst_l_5 = cv2.Laplacian(src, cv2.CV_32F, ksize=5)
dst_l_abs_5 =  cv2.convertScaleAbs(dst_l_5)



cv2.imshow('Src', src)
cv2.imshow('Laplacian - Dst 1x1', dst_l_abs_1)
cv2.imshow('Laplacian - Dst 3x3', dst_l_abs_3)
cv2.imshow('Laplacian - Dst 5x5', dst_l_abs_5)

cv2.waitKey(0)
cv2.destroyAllWindows()
