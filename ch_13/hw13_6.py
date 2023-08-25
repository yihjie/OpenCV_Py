import cv2

src = cv2.imread('macau.jpg', cv2.IMREAD_GRAYSCALE)

# 1. 降低噪音
#src = cv2.GaussianBlur(src, (3, 3), 0)

# Canny()
dst_c_true = cv2.Canny(src, 50, 100,L2gradient=True)
dst_c_false = cv2.Canny(src, 50, 100, L2gradient=False) # Default

cv2.imshow('Src', src)
cv2.imshow('Canny() - True', dst_c_true)
cv2.imshow('Canny() - False', dst_c_false) # Default ( abs(x) + abs(y) )

cv2.waitKey(0)
cv2.destroyAllWindows()
