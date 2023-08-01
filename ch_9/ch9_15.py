# cv2.THRESH_TOZERO_INV
'''
     if src > threshold:
         src = 0
     else
         src = src
'''

import cv2
import numpy as np

thresh = 127
maxval = 255

src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)

ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO_INV)

print(f"thresh = {thresh}, maxval = {maxval}, ret = {ret}")
print('-' * 80)
print(f"src = \n {src}")
print(f"dst = \n {dst}")
