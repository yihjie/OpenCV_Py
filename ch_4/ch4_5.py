# 顯示通道值

import cv2

pt_x, pt_y = 169, 118
img = cv2.imread("jk.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_color = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)

px_gray = img_gray[pt_x, pt_y]
px_bgr = img_color[pt_x, pt_y]

cv2.imshow("GRAY Color Space", img_gray)
cv2.imshow("BGR Color Space", img_color)
print(f"Gray Color 通道值 = {px_gray}")
print(f"BGR Color 通道值 = {px_bgr}")

cv2.waitKey(0)
cv2.destroyAllWindows()
