# modified the ch6_7.py

import cv2

img = cv2.imread('jk.jpg')
img_clone = img.copy()

# white
for z in range(115, 145):
    for y in range(110, 210):
        for x in range(0, 3):
            #img[z, y, x] = 255
            img.itemset((z, y, x), 255)

cv2.imshow("Original Image", img_clone)
cv2.imshow("Modified Image", img)

print(f"Before Modified - img[115, 110, 1] = {img_clone.item(115, 110, 1)}")
print(f" After Modified - img[115, 110, 1] = {img.item(115, 110, 1)}")
print("-" * 70)
print(f"Before Modified - img[125, 110, 1] = {img_clone.item(125, 110, 1)}")
print(f" After Modified - img[125, 110, 1] = {img.item(125, 110, 1)}")
print("-" * 70)
print(f"Before Modified - img[135, 110, 1] = {img_clone.item(135, 110, 1)}")
print(f" After Modified - img[135, 110, 1] = {img.item(135, 110, 1)}")

cv2.waitKey(0)
cv2.destroyAllWindows()
