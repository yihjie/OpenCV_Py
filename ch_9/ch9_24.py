# 建立 數位浮水印
'''
1. 取得原始影像的 row, column
2. 建立提取矩陣值為 254
3. 取得原始影像的 a0 影像
4. 建立與原始影像相同大小的浮水印影像
5. cv2.bitwise_or(原始影像, 浮水印影像)
'''


## 將浮水印影像嵌入原始影像
import cv2
import numpy as np

jk = cv2.imread('jk.jpg', cv2.IMREAD_GRAYSCALE)

row, column = jk.shape

h7 = np.ones((row, column), dtype=np.uint8) * 254
jk_a0 = cv2.bitwise_and(jk, h7)

watermark = cv2.imread('copyright.jpg', cv2.IMREAD_GRAYSCALE)

ret, wm = cv2.threshold(watermark, 0, 1, cv2.THRESH_BINARY)

# 將浮水印影像嵌入原始影像
water_jk = cv2.bitwise_or(jk_a0, wm)

cv2.imshow('Origin JK', jk)
cv2.imshow('JK_A0', jk_a0)
cv2.imshow('Watermark', watermark)
cv2.imshow("JK + Watermark", water_jk)

cv2.waitKey(0)
cv2.destroyAllWindows()
