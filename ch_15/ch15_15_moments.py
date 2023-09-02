import cv2
import numpy as np

src = cv2.imread('easy.jpg')
src_copy = src.copy()

# 1. convert to gray
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 2. convert to binary
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 3. find contours
contours, hierarchy = cv2.findContours(dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

n = len(contours)
imgList = []
for i in range(n):
    img = np.zeros(src.shape, np.uint8)
    imgList.append(img)

    # 列印輪廓點
    imgList[i] = cv2.drawContours(imgList[i], contours, i, (255, 255, 255), 5)
    cv2.imshow('contours' + str(i), imgList[i])

    # 列印輪廓面積
    area = cv2.moments(contours[i])
    print(f"輪廓面積 {i} = {area['m00']}")

    # 列印影像矩
    print(f"列印影像矩 {i}\n {area}")

cv2.imshow('Src', src_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()
