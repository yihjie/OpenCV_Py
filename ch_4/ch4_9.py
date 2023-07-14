# Split HSV
import cv2

image = cv2.imread("mountain.jpg")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hue, saturation, value = cv2.split(hsv_image)

cv2.imshow("BGR Color Space", image)
cv2.imshow("HSV Color Space", hsv_image)

cv2.imshow("Hue", hue)
cv2.imshow("Saturation", saturation)
cv2.imshow("Value", value)

cv2.waitKey(0)
cv2.destroyAllWindows()
