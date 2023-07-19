import cv2
import numpy as np

img = cv2.imread('jk.jpg')
money = cv2.imread('money.jpg')
money_clone = money.copy()
face = img[30:220, 80:250]      # 220 - 30 = 190 ; 250 - 80 = 170
money[30:220, 120:290] = face   # 220 - 30 = 190 ; 290 - 120 = 170
                                # 必須要同樣大小

cv2.imshow("Hung Image", img)
cv2.imshow("Money Origin", money_clone)
cv2.imshow("Money with Hung", money)

cv2.waitKey(0)
cv2.destroyAllWindows()
