import cv2
import numpy as np

height = 400
width  = 600
img = np.zeros((height, width, 3), np.uint8)

for i in range(0, 50):
    cx = np.random.randint(0, width)
    cy = np.random.randint(0, height)
    color = np.random.randint(0, 256, size=3).tolist()
    r = np.random.randint(5, 100)

    cv2.circle(img, (cx, cy), r, color, -1)

cv2.imshow("Random Circle", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
