# 判斷 q/Q 才能離開

import cv2

img = cv2.imread("jk.jpg")
cv2.imshow("MyPicture", img)
ret_value = cv2.waitKey(0)
if ret_value == ord('Q') or ret_value == ord('q'):
    cv2.destroyWindow("MyPicture")
    