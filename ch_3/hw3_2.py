import cv2
import numpy as np

img = cv2.imread("flower1.jpg")
img2 = np.hstack((img, img))
img_f = np.vstack((img2, img2))
cv2.imshow("Dst", img_f)
cv2.waitKey(0)
cv2.destroyAllWindows()
