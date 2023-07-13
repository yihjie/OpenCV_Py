
import cv2

img = cv2.imread('jk.jpg')
cv2.imshow('MyPicture', img)
ret_value = cv2.waitKey(0)
print(f"ret_value = {ret_value}")
