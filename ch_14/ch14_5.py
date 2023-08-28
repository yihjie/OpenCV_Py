# 反向運算
import cv2

src = cv2.imread('pengiun.jpg')

dst_down = cv2.pyrDown(src)
dst_up = cv2.pyrUp(dst_down)
dst_us = dst_up - src
dst = src - src

print(f"原始影像大小 =\n{src.shape}")
print(f"向下採樣大小 =\n{dst_down.shape}")
print(f"還原影像大小 =\n{dst_up.shape}")
print(f"差異 =\n{dst_us.shape}")
print(f"標準 =\n{dst.shape}")

cv2.imshow('Src', src)
cv2.imshow('Recovery', dst_up)
cv2.imshow('Recovery - Src', dst_us)
cv2.imshow('Src - Src', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
