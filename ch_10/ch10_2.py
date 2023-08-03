# cv2.resize()
# fx, fy
# dsize = None

import cv2

src = cv2.imread('southpole.jpg')

dst = cv2.resize(src, dsize=None, fx=0.5, fy=1.1)
cut_src = src[0:dst.shape[0], 0:dst.shape[1], :]

cv2.imshow("Src", src)
cv2.imshow("Fx=0.5, Fy=1.1", dst)
cv2.imshow("Cut- Src", cut_src)

print(f"src.shape = {src.shape}")
print(f"dst.shape = {dst.shape}")
print(f"cut_src.shape = {cut_src.shape}")

cv2.waitKey(0)
cv2.destroyAllWindows()
