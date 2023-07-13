# 以彩色 bmp 存檔
# 以灰階 bmp 存檔

import cv2

cv2.namedWindow("MyPicture")

img_color = cv2.imread("jk.jpg")
img_gray  = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("jk_color.bmp", img_color)
cv2.imwrite("jk_gray.bmp", img_gray)
