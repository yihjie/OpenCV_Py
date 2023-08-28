# Laplacian Pyramid, LP
import cv2
src = cv2.imread('pengiun.jpg')

G0 = src
G1 = cv2.pyrDown(src)
L0 = src - cv2.pyrUp(G1)

dst = L0 + cv2.pyrUp(G1)

print(f"src.shape=\n{src.shape}")
print(f"dst.shape=\n{dst.shape}")

cv2.imshow('Src', src)
cv2.imshow('L0', L0)
cv2.imshow('Dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
