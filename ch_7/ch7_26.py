import random

import cv2
import numpy as np

def OnChange(x):
    pass

def OnMouseAction(event, x, y, flags, param):
    color = np.random.randint(0, high=256, size=3).tolist()
    r = random.randint(10, 50)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x, y), r, color, thickness)

thickness = -1
height    = 400
width     = 600

image = np.ones((height, width, 3), np.uint8) * 255

cv2.namedWindow("Draw Circle")
cv2.setMouseCallback("Draw Circle", OnMouseAction)
cv2.createTrackbar('Thickness', 'Draw Circle', 0, 1, OnChange)

while 1:
    cv2.imshow("Draw Circle", image)

    key = cv2.waitKey(100)
    num = cv2.getTrackbarPos('Thickness', 'Draw Circle')
    if num == 0:
        thickness = -1
    else:
        thickness = 3

    if key == ord('Q') or key == ord('q'):
        break

cv2.destroyAllWindows()
