import cv2
import numpy as np

img = cv2.imread('antarctic.jpg')

cy = int(img.shape[0] / 2)
cx = int(img.shape[1] / 2)

size = (200, 100)

for i in range(0, 15):
    angle = np.random.randint(0, 361)                       # 橢圓偏移的角度
    color = np.random.randint(0, 256, size=3).tolist()
    cv2.ellipse(img, (cx, cy), size, angle, 0, 360, color, 1)
    # cv2,ellipse(圖形, 圓心座標, 軸長, 偏移角度, 圓弧起點角度, 圓弧終點角度, 顏色, 線粗)

cv2.imshow("My Ellipse", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
