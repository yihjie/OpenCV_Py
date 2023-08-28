import cv2

src = cv2.imread('pengiun.jpg')

dst1 = src + src
dst2 = src - src

cv2.imshow('Src', src)
cv2.imshow('Src ADD', dst1)
cv2.imshow('Src SUBTRACTION', dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()
