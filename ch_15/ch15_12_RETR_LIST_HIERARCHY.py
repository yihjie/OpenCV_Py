import cv2

src = cv2.imread('easy2.jpg')
src_copy = src.copy()

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 5)

print(f"hierarchy datatype : {type(hierarchy)}")
print(f"Level : \n{hierarchy}")

cv2.imshow('Src', src_copy)
cv2.imshow('Result', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
