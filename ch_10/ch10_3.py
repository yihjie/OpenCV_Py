# dst = cv2.flip(src, flipCode)

import cv2

src = cv2.imread('python.jpg')

dst_x = cv2.flip(src, 0)
dst_y = cv2.flip(src, 1)
dst_xy = cv2.flip(src, -1)

cv2.imshow("Src", src)
cv2.imshow("Flip Vertically (X)", dst_x)
cv2.imshow("Flip Horizontally (Y)", dst_y)
cv2.imshow("Flip Vertically & Horizontally (XY)", dst_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()
