# Canny

import cv2

#src = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('lena.jpg')
dst1 = cv2.Canny(src, 50, 100)
dst2 = cv2.Canny(src, 50, 200)

cv2.imshow('Src', src)
cv2.imshow('Canny(50, 100)', dst1)
cv2.imshow('Canny(50, 200)', dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()
