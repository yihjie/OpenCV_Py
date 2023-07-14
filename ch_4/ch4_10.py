# 合併 BGR 通道的影像
import cv2

image = cv2.imread('street.jpg')
blue, green, red = cv2.split(image)
bgr_image = cv2.merge([blue, green, red])
rgb_image = cv2.merge([red, green, blue])
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.imshow("Orginal - BGR Color Space", image)
cv2.imshow("RGB Color Space", image_rgb)
cv2.imshow("B->G->R merge", bgr_image)
cv2.imshow("R->G->B merge", rgb_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
