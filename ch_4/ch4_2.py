import cv2

img = cv2.imread("view.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

cv2.imshow("view.jpg", img)
cv2.imshow("RGB Color Space", img_rgb)
cv2.imshow("BGR Color Space", img_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()
