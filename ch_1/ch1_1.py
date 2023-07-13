# 觀察讀取檔案的回傳值

import cv2

img1 = cv2.imread("jk.jpg")
print(f"讀取成功 ： {type(img1)}")
img2 = cv2.imread("none.jpg")
print(f"讀取失敗 ： {type(img2)}")
