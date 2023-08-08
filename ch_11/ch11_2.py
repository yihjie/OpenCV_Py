# 方框濾波器函數
# dst = cv2.boxFilter(src, ddepth, ksize, anchor, normalize, borderType)
import cv2

src = cv2.imread('hung.jpg')

# normalize = 0 ( 不進行歸一化 )
dst1 = cv2.boxFilter(src, ddepth=-1, ksize=(2, 2), normalize=0)
dst2 = cv2.boxFilter(src, ddepth=-1, ksize=(3, 3), normalize=0)
dst3 = cv2.boxFilter(src, ddepth=-1, ksize=(5, 5), normalize=0)

# normalize = 1 ( 進行歸一化 ) 結果同 blur()
dst1n = cv2.boxFilter(src, ddepth=-1, ksize=(2, 2), normalize=1)
dst2n = cv2.boxFilter(src, ddepth=-1, ksize=(3, 3), normalize=1)
dst3n = cv2.boxFilter(src, ddepth=-1, ksize=(5, 5), normalize=1)

cv2.imshow('Src', src)
cv2.imshow('Dst - 2x2', dst1)
cv2.imshow('Dst - 3x3', dst2)
cv2.imshow('Dst - 5x5', dst3)
cv2.imshow('Dst Normal - 2x2', dst1n)
cv2.imshow('Dst Normal - 3x3', dst2n)
cv2.imshow('Dst Normal - 5x5', dst3n)

cv2.waitKey(0)
cv2.destroyAllWindows()
