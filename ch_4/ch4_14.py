# modify Value (亮度)

import cv2

image = cv2.imread('street.jpg')
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hue, saturation, value = cv2.split(image_hsv)
print(f"Original value : \n{saturation}")
value.fill(255)
print(f"Modified value : \n{hue}")
hsv_image = cv2.merge([hue, saturation, value])
new_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

cv2.imshow("Original BGR Color Space", image)
cv2.imshow("HSV Color Space", image_hsv)
cv2.imshow("Modified HSV Color Space", hsv_image)
cv2.imshow("Modified HSV to BGR Color Space", new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
