import cv2
import numpy as np

src = np.zeros((300, 300, 3), np.uint8)
cx = int(src.shape[1] / 2)
cy = int(src.shape[0] / 2)
cv2.circle(src, (cx, cy), 120, (255,255,255), -1)

dst_x = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dst_x_a = cv2.convertScaleAbs(dst_x)
dst_y = cv2.Sobel(src, cv2.CV_32F, 0, 1)
dst_y_a = cv2.convertScaleAbs(dst_y)
dst = cv2.addWeighted(dst_x_a, 0.5, dst_y_a, 0.5, 0)

cv2.imshow('Src', src)
cv2.imshow('Dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
