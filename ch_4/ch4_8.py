# colorbar to split(B, G, R)

import cv2

image = cv2.imread("mountain.jpg")
blue, green, red = cv2.split(image)

cv2.imshow("bgr", image)
cv2.imshow("blue", blue)
cv2.imshow("green", green)
cv2.imshow("red", red)

print(f"image 通道影像屬性 shape = {image.shape}")
print(f"B 通道影像屬性 shape = {blue.shape}")
print(f"G 通道影像屬性 shape = {green.shape}")
print(f"R 通道影像屬性 shape = {red.shape}")

cv2.waitKey(0)
cv2.destroyAllWindows()
