import cv2

image = cv2.imread("mountain.jpg")
blue, green, red = cv2.split(image)

print(f"image 通道影像內容 = {image}")
print(f"B 通道影像內容 = {blue}")
print(f"G 通道影像內容 = {green}")
print(f"R 通道影像內容 = {red}")

cv2.waitKey(0)
cv2.destroyAllWindows()
