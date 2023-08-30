import cv2
import numpy as np

src = cv2.imread('easy3.jpg')
src_copy = src.copy()
src_0 = src.copy()
src_1 = src.copy()
src_2 = src.copy()
src_3 = src.copy()
src_l = [src_0, src_1, src_2, src_3]


src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(dst_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 5)

imgList = []
n = len(contours)
for i in range(n):
    img = np.zeros(src.shape, np.uint8)  # 建立輪廓影像
    imgList.append(img)  # 將預設黑底影像加入串列
    imgList[i] = cv2.drawContours(src_l[i], contours, i, (0, 255, 0), 5)
    cv2.imshow('Result - Hierarchy - ' + str(i), imgList[i])

print(f"hierarchy datatype : {type(hierarchy)}")
print(f"Level : \n{hierarchy}")

cv2.imshow('Src', src_copy)
cv2.imshow('Result', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
