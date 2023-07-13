# 修改一個區塊的影像像素 BGR
import cv2

img = cv2.imread("dog.jpg")
cv2.imshow("Original Image", img)
for y in range(img.shape[0] - 50, img.shape[0]):
    for x in range(img.shape[1] - 50, img.shape[1]):
        img[y, x] = [255, 255, 255]
cv2.imshow("After the change", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
