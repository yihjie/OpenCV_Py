# 顯示影像

import cv2

img = cv2.imread("jk.jpg")
cv2.imshow("MyPicture", img)
ret_value = cv2.waitKey(0)
cv2.destroyWindow("MyPicture")
