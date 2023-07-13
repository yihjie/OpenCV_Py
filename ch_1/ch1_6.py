# 更改視窗大小
# 灰階顯示

import cv2

cv2.namedWindow("MyPicture1")
cv2.namedWindow("MyPicture2", cv2.WINDOW_NORMAL)

img1 = cv2.imread("jk.jpg")
img2 = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("MyPicture1", img1)
cv2.imshow("MyPicture2", img2)
cv2.waitKey(3000)
cv2.destroyWindow("MyPicture1")
cv2.waitKey(3000)
cv2.destroyAllWindows()
