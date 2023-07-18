# 產生白色長條遮住眼睛部位
import cv2

img = cv2.imread('jk.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow("Before modified", img)
for y in range(120, 140):
    for x in range(110, 210):
        img[y, x] = 255
cv2.imshow("After modified", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
