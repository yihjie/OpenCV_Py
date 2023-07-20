import cv2
import numpy as np

img = np.ones((350, 500, 3), np.uint8) * 255

cv2.rectangle(img, (1, 1), (300, 300), (255, 0, 0))         # 畫矩形

for x in range(150, 300, 10):
    cv2.line(img, (x, 1), (300, x - 150), (0, 255, 0))      # 綠
for y in range(150, 300, 10):
    cv2.line(img, (1, y), (y - 150, 300), (0, 0, 255))      # 紅

cv2.imshow("My Draw", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
