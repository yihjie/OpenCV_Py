import cv2
import numpy as np

img = np.ones((300, 300, 3), np.uint8) * 255

cv2.line(img, (10, 75), (200, 75), (255, 0, 0), thickness=18, lineType=cv2.LINE_4)
cv2.line(img, (10, 150), (200, 150), (0, 255, 0), thickness=18, lineType=cv2.LINE_8)
cv2.line(img, (10, 225), (200, 225), (0, 0, 255), thickness=18, lineType=cv2.LINE_AA)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
