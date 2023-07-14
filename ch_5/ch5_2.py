# 建立一個 160 x 280 的 白色影像
import cv2
import numpy as np

height = 160
width = 280

# 建立GRAY影像陣列
image = np.zeros((height, width), np.uint8)
image.fill(255)

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
