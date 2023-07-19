import cv2
import numpy as np

img = cv2.imread('jk.jpg')
img_clone = img.copy()
face = img[30:220, 80:250]      # 220 - 30 = 190 ; 250 - 80 = 170
img_clone[:, :, :] = 255
img_clone[30:220, 80:250] = face

cv2.imshow("Hung Image", img)
cv2.imshow("White with Hung", img_clone)

cv2.waitKey(0)
cv2.destroyAllWindows()
