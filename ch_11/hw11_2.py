import cv2

src = cv2.imread('antar.jpg')

dst_median = cv2.medianBlur(src, 3)
dst_Gauss = cv2.GaussianBlur(src,(3, 3), 0, 0)

cv2.imshow('Src', src)
cv2.imshow('median Dst 3', dst_median )
cv2.imshow('Gaussian Dst 3x3', dst_Gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()
