# image encryption and decryption

import cv2
import numpy as np

src = cv2.imread('forest.jpg')

key = np.random.randint(0, 256, src.shape, np.uint8)

cv2.imshow('forest', src)
cv2.imshow('secret', key)
print(src.shape)

img_encry = cv2.bitwise_xor(src, key)
img_decry = cv2.bitwise_xor(img_encry, key)

cv2.imshow("Encryption", img_encry)
cv2.imshow("Decryption", img_decry)

cv2.waitKey(0)
cv2.destroyAllWindows()
