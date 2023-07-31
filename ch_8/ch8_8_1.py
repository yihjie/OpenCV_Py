import cv2
import numpy as np

g = np.zeros((200, 300, 3), np.uint8)
r = np.zeros((200, 300, 3), np.uint8)
m = np.zeros((200, 300, 1), np.uint8)

g[:, :, 1] = 255                 # G channel = 255
r[:, :, 2] = 255                 # R channel = 255
m[50:150, 100:200, :] = 255      # mask , 非 0 即可，只是為了方便顯示，設定為 255 (白)

g_r = cv2.add(g, r)
g_r_m = cv2.add(g, r, mask=m)

cv2.imshow("G", g)
cv2.imshow("R", r)
cv2.imshow("Mask", m)
cv2.imshow("G + R", g_r)
cv2.imshow("G + R with Mask", g_r_m)

cv2.waitKey(0)
cv2.destroyAllWindows()
