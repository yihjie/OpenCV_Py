# 多邊形 ( Polylines )
import cv2
import numpy as np

img1 = np.ones((200, 300, 3), np.uint8) * 255
img2 = np.ones((200, 300, 3), np.uint8) * 255

blue = (255, 0, 0)
red = (0, 0, 255)

pts = np.array([[150, 50],[250, 100],[150, 150], [50, 100]])

cv2.polylines(img1, [pts], True, blue, 5)
cv2.polylines(img2, [pts], False, red, 5)

cv2.imshow("is_Closed : True", img1)
cv2.imshow("is_Closed : False", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
