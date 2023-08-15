import cv2

src = cv2.imread('border.jpg')

dst_b3 = cv2.bilateralFilter(src, 3, 100, 100)
dst_b7 = cv2.bilateralFilter(src, 7, 100, 100)

dst_m3 = cv2.blur(src, (3, 3))
dst_m7 = cv2.blur(src, (7, 7))

cv2.imshow('Src', src)
cv2.imshow('Bilateral 3x3', dst_b3)
cv2.imshow('Bilateral 7x7', dst_b7)
cv2.imshow('Mean 3x3', dst_m3)
cv2.imshow('Mean 7x7', dst_m7)

cv2.waitKey(0)
cv2.destroyAllWindows()
