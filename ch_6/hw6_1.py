# modify ch6_7.py and reference ch6_7_1.py

import cv2

img = cv2.imread('jk.jpg')
img_clone = img.copy()


img[115:125, 110:210] = [255, 0 ,255]   # purple
img[125:135, 110:210] = 255             # white
img[135:145, 110:210] = [0, 255, 255]   # yellow

cv2.imshow("Original Image", img_clone)
cv2.imshow("Modified Image", img)

print(f"Before Modified - img[115, 110] = {img_clone[115, 110]}")
print(f" After Modified - img[115, 110] = {img[115, 110]}")
print("-" * 70)
print(f"Before Modified - img[125, 110] = {img_clone[125, 110]}")
print(f" After Modified - img[125, 110] = {img[125, 110]}")
print("-" * 70)
print(f"Before Modified - img[135, 110] = {img_clone[135, 110]}")
print(f" After Modified - img[135, 110] = {img[135, 110]}")

cv2.waitKey(0)
cv2.destroyAllWindows()
