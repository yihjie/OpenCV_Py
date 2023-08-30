# modified ch15_1.py
# separe draw each hierarchy

import cv2
import numpy as np

src = cv2.imread('easy.jpg')
src_copy = src.copy()
# 1.
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 2.
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 3.
contours, hierarchy = cv2.findContours(dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 4. draw all contours
#dst = cv2.drawContours(src, contours, -1, (0, 255,0), 5)


cv2.imshow('Src', src)
# 4. draw each hierarchy
n = len(contours)                                   # 回傳輪廓數
imgList = []                                        # 建立輪廓串列
for i in range(n):                                  # 依次繪製輪廓
    img = np.zeros(src.shape, np.uint8)             # 建立輪廓影像
    imgList.append(img)                             # 將預設黑底影像加入串列
    # 4.1 draw contours
    imgList[i] = cv2.drawContours(imgList[i], contours, i, (255, 255, 255), 5)
    cv2.imshow('contours ' + str(i), imgList[i])    # 顯示輪廓影像

cv2.waitKey(0)
cv2.destroyAllWindows()
