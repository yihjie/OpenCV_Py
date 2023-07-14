# Alpha 通道 (透明度)
import cv2

image = cv2.imread('street.jpg')
image_bgra = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
blue, green, red, alpha = cv2.split(image_bgra)
print("列出轉成含A通道影像物件後的 alpha 值")
print(alpha)
cv2.imshow("Original", image)
cv2.imshow("Original with Alpha", image_bgra)
alpha.fill(32)
a32_image = cv2.merge([blue, green, red, alpha])
cv2.imshow("Alpha = 32", a32_image)

alpha.fill(128)
a128_image = cv2.merge([blue, green, red, alpha])
cv2.imshow("Alpha = 128", a128_image)

cv2.imwrite('a32.png', a32_image)
cv2.imwrite('a128.png', a128_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
