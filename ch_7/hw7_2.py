# Modified ch7_12.py

import cv2
import numpy as np

img = np.ones((480, 600, 3), np.uint8 ) * 255

cy = int(img.shape[0] / 2)
cx = int(img.shape[1] / 2)

size = (200, 100)

for i in range(0, 20):
    angle = np.random.randint(0, 361)                       # 橢圓偏移的角度
    color = np.random.randint(0, 256, size=3).tolist()
    thickness = np.random.randint(0, 5)
    cv2.ellipse(img, (cx, cy), size, angle, 0, 360, color, thickness)
    # cv2,ellipse(圖形, 圓心座標, 軸長, 偏移角度, 圓弧起點角度, 圓弧終點角度, 顏色, 線粗)

cv2.imshow("My Ellipse", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
