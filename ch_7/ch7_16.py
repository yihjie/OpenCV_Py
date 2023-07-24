# 含倒影的文字

import cv2
import numpy as np

img = np.ones((300, 600, 3), np.uint8) * 255

font = cv2.FONT_HERSHEY_SIMPLEX

blue = (255, 0, 0)
green = (0, 255, 0)

cv2.putText(img, 'Python', (120, 120), font, 3, blue, 12)
cv2.putText(img, 'Python', (120, 180), font, 3, green, 12, cv2.LINE_8, True)

cv2.imshow("Python", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
