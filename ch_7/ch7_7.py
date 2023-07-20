import cv2

img = cv2.imread('antarctic.jpg')

cy = int(img.shape[0] / 2)      # 中心點 y 座標
cx = int(img.shape[1] / 2)      # 中心點 x 座標

red = (0, 0, 255)
yellow = (0, 255, 255)

cv2.circle(img, (cx, cy), 30, red, -1)

for r in range(40, 200, 20):
    cv2.circle(img, (cx, cy), r, yellow, 2)

cv2.imshow("My Draw", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
