# 反彈球動畫練習
# 水平位移速度改為隨機

import cv2
import numpy as np
from random import *
import time

width  = 640                    # 畫布寬
height = 480                    # 畫布長

speed = 0.01                    # 球的移動速度

r = 15                          # 球的半徑
x = 50                          # 球心的初始座標
y = 50                          # 球心的初始座標
random_step = [3, 4, 5, 6, 7]   #  x 步伐陣列
shuffle(random_step)            # 隨機 x 步伐
x_step = random_step[0]
y_step = 5

print(x_step)
while cv2.waitKey(1) == -1:
    if x > width - r or x < r:
        x_step = -x_step
    if y > height - r or y < r:
        y_step = -y_step
    x += x_step
    y += y_step

    img = np.ones((height, width, 3), np.uint8) * 255

    cv2.circle(img, (x, y), r, (0, 0, 255), -1)

    cv2.imshow("Bouncing Ball", img)

    time.sleep(speed)

cv2.destroyAllWindows()
