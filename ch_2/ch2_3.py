# 顯示特定影像像素座標的 BGR 值
import cv2

img = cv2.imread("dog.jpg")

pt_x = 169
pt_y = 118

px = img[pt_x, pt_y]
print(f"更改前的 BGR = {px}")
px = [255, 255, 255]
print(f"更改後的 BGR = {px}")
