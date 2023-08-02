# Least significiant bit ( 最低有效位元 ) --> 對影像的影響最小
# 常見的數位浮水印便是藏在 A0 平面影像

import cv2
import numpy as np

jk = cv2.imread('jk.jpg', cv2.IMREAD_GRAYSCALE)

# 取得 jk 的 row, column
row, column = jk.shape

# 建立像素值為 254 的影像
h7 = np.ones((row, column), dtype=np.uint8) * 254

# 建立數位浮水印 cv2.bitwise_and( jk, h7 )
new_jk = cv2.bitwise_and(jk, h7)

cv2.imshow("Origin JK", jk)
cv2.imshow("waterprint - h7", h7)
cv2.imshow("New JK", new_jk)

cv2.waitKey(0)
cv2.destroyAllWindows()
