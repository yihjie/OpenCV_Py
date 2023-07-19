import cv2
import numpy as np

img = np.ones((350, 500, 3), np.uint8) * 255            # 建立白色底的畫布

cv2.line(img, (1, 1), (300, 1), (255, 0, 0))            # 上方水平直線 藍
cv2.line(img, (1, 300), (300, 300), (255, 0, 0))        # 下方水平直線 藍
cv2.line(img, (300, 1), (300, 300), (255, 0, 0))        # 右方垂直直線 藍
cv2.line(img, (1, 1), (1, 300), (255, 0, 0))            # 左方垂直直線 藍

cv2.imshow("My Draw", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
