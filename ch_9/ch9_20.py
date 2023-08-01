import cv2

maxval = 255
thresh1 = 127
thresh2 =  80


src = cv2.imread('jk.jpg', cv2.IMREAD_GRAYSCALE)

ret1, dst1 = cv2.threshold(src, thresh1, maxval, cv2.THRESH_BINARY)
ret2, dst2 = cv2.threshold(src, thresh2, maxval, cv2.THRESH_BINARY)
ret3, dst3 = cv2.threshold(src,thresh2, maxval, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("Original Image", src)
cv2.imshow(f"DST - {thresh1}", dst1)
cv2.imshow(f"DST - {thresh2}", dst2)
cv2.imshow(f"OSTU -{ret3}", dst3)

print(f"thresh1     : {ret1}")
print(f"thresh2     : {ret2}")
print(f"otsu thresh : {ret3}")

cv2.waitKey(0)
cv2.destroyAllWindows()
