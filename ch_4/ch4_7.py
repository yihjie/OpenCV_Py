# colorbar to split(B, G, R)

import cv2

image = cv2.imread("colorbar.jpg")
blue, green, red = cv2.split(image)

cv2.imshow("bgr", image)
cv2.imshow("blue", blue)
cv2.imshow("green", green)
cv2.imshow("red", red)

print(f"B 通道影像屬性 shape = {blue.shape}")
print("列印 B 通道內容")
print(blue)
print("-" * 70)
print(f"G 通道影像屬性 shape = {green.shape}")
print("列印 G 通道內容")
print(green)
print("-" * 70)
print(f"R 通道影像屬性 shape = {red.shape}")
print("列印 R 通道內容")
print(red)

cv2.waitKey(0)
cv2.destroyAllWindows()
