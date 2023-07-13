# 列印彩色影像的屬性
import cv2

img = cv2.imread("dog.jpg")
img_g = cv2.imread("dog.jpg", cv2.IMREAD_GRAYSCALE)
print("列印彩色影像的屬性")
print(f"shape = {img.shape}")
print(f"size  = {img.size}")
print(f"dtype = {img.dtype}")
print("--------------------")
print("列印灰階影像的屬性")
print(f"shape = {img_g.shape}")
print(f"size  = {img_g.size}")
print(f"dtype = {img_g.dtype}")
print("--------------------")
print(180 * 322 * 3)
print(180 * 322 * 1)
