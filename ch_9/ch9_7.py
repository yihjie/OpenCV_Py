# cv2.THRESH_BINARY_INV
## cv2.THRESH_BINARY
'''
    if src > thresh:
        src = maxval
    else:
        src = 0
'''
## cv2.THRESH_BINARY_INV
'''
    if src > thresh:
        src = 0
    else:
        src = maxval
'''

import cv2

maxval = 255
thresh1 = 127
thresh2 =  80

src = cv2.imread('jk.jpg')

ret1, dst1 = cv2.threshold(src, thresh1, maxval, cv2.THRESH_BINARY_INV)
ret11, dst11 = cv2.threshold(src, thresh1, maxval, cv2.THRESH_BINARY)
ret2, dst2 = cv2.threshold(src, thresh2, maxval, cv2.THRESH_BINARY_INV)
ret22, dst22 = cv2.threshold(src, thresh2, maxval, cv2.THRESH_BINARY)

cv2.imshow("Original Image", src)
cv2.imshow(f"INV - DST - {thresh1}", dst1)
cv2.imshow(f"DST - {thresh1}", dst11)
cv2.imshow(f"INV - DST - {thresh2}", dst2)
cv2.imshow(f"DST - {thresh2}", dst22)

print(f"thresh1 : {thresh1}\nret1 : {ret1}")
print(f"thresh2 : {thresh2}\nret2 : {ret2}")

cv2.waitKey(0)
cv2.destroyAllWindows()
