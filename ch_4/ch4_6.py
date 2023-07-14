# BGR to HSV
import cv2

img = cv2.imread("mountain.jpg")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("BGR Color Space", img)
cv2.imshow("HSV Color Space", img_hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()
