# List contours hiarchary counter

import cv2

src = cv2.imread('easy.jpg')
# 1. convert to gray
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 2. convert to binary
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 3. find contours
contours, hierarchy = cv2.findContours(dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

n = len(contours)
for i in range(n):
    print(f"編號 = {i}")
    print(f"輪廓點數量 = {len(contours[i])}")
    print(f"輪廓點的外形 = {contours[i].shape}")
    print('-' * 80)

print(contours[1])
