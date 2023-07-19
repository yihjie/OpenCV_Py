import cv2

img = cv2.imread('street.png', cv2.IMREAD_UNCHANGED)
img_clone = img.copy()

img[0:200, 0:200, 3] = 128
cv2.imwrite('street128_1.png', img)
img_2 = cv2.imread('street128.png', cv2.IMREAD_UNCHANGED)

print(f"修改前 img[10, 50] = {img_clone[10, 50]}")
print(f"修改後 img[10, 50] = {img[10, 50]}")
print("-" * 70)
print(f"修改前 img[50, 99] = {img_clone[50, 99]}")
print(f"修改後 img[50, 99] = {img[50, 99]}")

cv2.imshow('Original Image', img)
cv2.imshow('Modified Image', img_2)     # OpenCV 無法顯示 alpha

cv2.waitKey(0)
cv2.destroyAllWindows()
