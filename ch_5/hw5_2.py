# modify ch5_10.py
# change the display from horziation to verical
import cv2
import numpy as np

height = 150
width = 300

image = np.zeros((height, width, 3), np.uint8)
image[:, 0:100, 0] = 255  # blue
image[:, 100:200, 1] = 255  # green
image[:, 200:300, 2] = 255  # red

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
