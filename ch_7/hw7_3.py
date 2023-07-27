# Modified ch7_23.py
# 建立隨機圖

import cv2
import numpy as np

def OnMouseAction(event, x, y, flags, param):
    color = np.random.randint(0, high=256, size=3).tolist()          # 產生隨機色彩
    px = np.random.randint(10, 600)
    py = np.random.randint(10, 400)

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image, (x, y), (px, py), color, -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(image, (x, y), (px, py), color, 3)

height = 400
width  = 600

image = np.ones((height, width, 3), np.uint8) * 255

cv2.namedWindow("Draw Rectangle")
cv2.setMouseCallback("Draw Rectangle", OnMouseAction)

while 1:
    cv2.imshow("Draw Rectangle", image)
    key = cv2.waitKey(100)

    if key == ord('Q') or key == ord('q'):
        break

cv2.destroyAllWindows()
