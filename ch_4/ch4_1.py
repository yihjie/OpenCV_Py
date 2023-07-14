import cv2

img = cv2.imread("view.jpg")
cv2.imshow("view.jpg", img)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB Color Space", img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()
