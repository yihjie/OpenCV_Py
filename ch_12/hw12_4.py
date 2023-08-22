# custom kernel
# gradient

import cv2

src = cv2.imread('calculus.jpg')
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 21))

dst = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('Src', src)
cv2.imshow('Result', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
