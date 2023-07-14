# BGR-> HSV, split and merge
import cv2

image = cv2.imread('street.jpg')
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hue, saturation, value = cv2.split(image_hsv)
hsv_image = cv2.merge([hue, saturation, value])

cv2.imshow("Original BGR Space", image)
cv2.imshow("HSV Color Space", image_hsv)
cv2.imshow("H->S->V merge", hsv_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
