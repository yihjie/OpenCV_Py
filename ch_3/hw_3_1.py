import cv2
import numpy as np

img = cv2.imread("huang.jpg")
img2 = np.hstack((img, img))
cv2.imshow("Dst", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
