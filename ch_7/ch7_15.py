import cv2
import numpy as np

img = np.ones((300, 600, 3), np.uint8) * 255

font = cv2.FONT_HERSHEY_SIMPLEX

blue = (255, 0, 0)
yellow = (0, 255, 255)
red = (0, 0, 255)

cv2.putText(img, 'Python', (150, 180), font, 3, red, 20)
cv2.putText(img, 'Python', (150, 180), font, 3, blue, 12)
cv2.putText(img, 'Python', (150, 180), font, 3, yellow, 5)


cv2.imshow("Python Text", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
