# 建立隨機圖 ( 圓形、矩形 )

import cv2
import numpy as np

def OnMouseAction(event, x, y, flags, param):
    color = np.random.randint(0, high=256, size=3).tolist()          # 產生隨機色彩

    if event == cv2.EVENT_LBUTTONDOWN:
        r = np.random.randint(10, 50)  # 產生半徑 10~50 的圓
        if key == ord('s') or key == ord('S'):
            cv2.circle(image, (x, y), r, color, -1)                    # 實心圓
        else:
            cv2.circle(image, (x, y), r, color, 3)            # 空心圓
    elif event == cv2.EVENT_RBUTTONDOWN:
        px = np.random.randint(10, 100)
        py = np.random.randint(10, 100)
        if key == ord('s') or key == ord('S'):
            cv2.rectangle(image, (x, y), (px, py), color, -1)
        else:
            cv2.rectangle(image, (x, y), (px, py), color, 3)


height = 400
width  = 600

image = np.ones((height, width, 3), np.uint8) * 255

cv2.namedWindow("My Draw")
cv2.setMouseCallback("My Draw", OnMouseAction)

while 1:
    cv2.imshow("My Draw", image)
    key = cv2.waitKey(100)

    if key == ord('Q') or key == ord('q'):
        break

cv2.destroyAllWindows()
