
import cv2

img_src = cv2.imread('mazu.jpg')

img_add = img_src + img_src
img_cv2 = cv2.add(img_src, img_src)
img_cv3 = cv2.addWeighted(img_cv2,1, img_src, -1.0,0)
img_cv4 = cv2.addWeighted(img_add, 1, img_src, -1.0, 0)

cv2.imshow("Origin Mazu", img_src)
cv2.imshow("Add Mazu", img_add)
cv2.imshow("cv2.add Mazu", img_cv2)
cv2.imshow("img_cv2_add - img_src", img_cv3)
cv2.imshow("img_add - img_src", img_cv4)

cv2.waitKey(0)
cv2.destroyAllWindows()
