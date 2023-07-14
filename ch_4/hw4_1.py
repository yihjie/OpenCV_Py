import cv2

image = cv2.imread('coffee.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hue, saturation, value = cv2.split(image_hsv)

cv2.imshow('bgr', image)
cv2.imshow('RGB', image_rgb)
cv2.imshow('saturation', saturation)
cv2.imshow('value', value)

cv2.waitKey(0)
cv2.destroyAllWindows()
