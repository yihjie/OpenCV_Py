# 驗證 Hu(0) = M(nu20) + M(nu02)

import cv2

src = cv2.imread('heart.jpg')
src_copy = src.copy()
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

M = cv2.moments(src_gray)
nu20 = M['nu20']
nu02 = M['nu02']

Hu = cv2.HuMoments(M)

result = Hu[0][0] - (nu20 + nu02)

print(f"歸一化中心矩 nu20 = {nu20}")
print(f"歸一化中心矩 nu02 = {nu02}")
print(f"Hu = \n{Hu}")
print(f"Hu[0][0] = {Hu[0][0]}")

print(f"驗證結果 h0 - (nu20 + nu02) = {result}")
