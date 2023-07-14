# BGR-> HSV, split and merge
import cv2

image = cv2.imread('street.jpg')
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hue, saturation, value = cv2.split(image_hsv)
svh_image = cv2.merge([saturation, value, hue])
vhs_image = cv2.merge([value, hue, saturation])

cv2.imshow("S V H", svh_image)
cv2.imshow("V H S", vhs_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
