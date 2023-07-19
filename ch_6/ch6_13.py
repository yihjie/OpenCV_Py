# 擷取影像感興趣區塊 ( Region of Interest, ROI )

import cv2

img = cv2.imread('jk.jpg')      # 彩色讀取
face = img[30:220 , 80:250]     # ROI

cv2.imshow("Hung Image", img)   # 整張影像
cv2.imshow("Face", face)        # ROI

cv2.waitKey(0)
cv2.destroyAllWindows()
