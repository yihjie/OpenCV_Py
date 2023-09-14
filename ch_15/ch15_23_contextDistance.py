# modified from ch15_22_matchShapes.py to calc ShapeContextDistance
import cv2

# Read and Create image src1
src1 = cv2.imread('mycloud1.jpg')
src1_copy = src1.copy()
src1_gray = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
ret1, dst_binary1 = cv2.threshold(src1_gray, 127, 255, cv2.THRESH_BINARY)
contours1, hierarchy1 = cv2.findContours(dst_binary1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt1 = contours1[0]

# Read and Create image src2
src2 = cv2.imread('mycloud2.jpg')
src2_copy = src2.copy()
src2_gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)
ret2, dst_binary2 = cv2.threshold(src2_gray, 127, 255, cv2.THRESH_BINARY)
contours2, hierarchy2 = cv2.findContours(dst_binary2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt2 = contours2[0]

# Read and Create image src3
src3 = cv2.imread('explode1.jpg')
src3_copy = src3.copy()
src3_gray = cv2.cvtColor(src3, cv2.COLOR_BGR2GRAY)
ret3, dst_binary3 = cv2.threshold(src3_gray, 127, 255, cv2.THRESH_BINARY)
contours3, hierarchy3 = cv2.findContours(dst_binary3, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt3 = contours3[0]

sd = cv2.createShapeContextDistanceExtractor()

match11 = sd.computeDistance(cnt1, cnt1)
match12 = sd.computeDistance(cnt1, cnt2)
match13 = sd.computeDistance(cnt1, cnt3)
match23 = sd.computeDistance(cnt2, cnt3)

print(f"src1 vs src1 = {match11}")
print(f"src1 vs src2 = {match12}")
print(f"src1 vs src3 = {match13}")
print(f"src2 vs src3 = {match23}")

cv2.imshow('Src1', src1_copy)
cv2.imshow('Src2', src2_copy)
cv2.imshow('Src3', src3_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()
