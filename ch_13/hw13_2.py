import cv2
import numpy as np

src = np.zeros((300, 300, 3), np.uint8)
cx = int(src.shape[1] / 2)
cy = int(src.shape[0] / 2)
cv2.circle(src, (cx, cy), 120, (255,255,255), -1)

dst_y = cv2.Sobel(src, cv2.CV_32F, 0, 1)
dst_y_a = cv2.convertScaleAbs(dst_y)

cv2.imshow('Src', src)
cv2.imshow('dst_8u', dst_y)
cv2.imshow('dst_y', dst_y_a)

cv2.waitKey(0)
cv2.destroyAllWindows()
