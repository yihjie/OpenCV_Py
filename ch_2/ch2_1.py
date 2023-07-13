# 列印灰階影像的屬性
import cv2

img = cv2.imread("dog.jpg", cv2.IMREAD_GRAYSCALE)
print("列印灰階影像的屬性")
print(f"shape = {img.shape}")
print(f"size  = {img.size}")
print(f"dtype = {img.dtype}")
