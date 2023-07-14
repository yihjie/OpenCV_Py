# 彩色轉灰階 cv2.COLOR_BGR2GRAY

import cv2

img = cv2.imread("jk.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("BGR Color Space", img)
cv2.imshow("GRAY Color Space", img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
