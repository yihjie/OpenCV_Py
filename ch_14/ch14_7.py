# Laplacian Pyramid, LP

import cv2

src = cv2.imread('pengiun.jpg')


G0 = src
G1 = cv2.pyrDown(src)
G2 = cv2.pyrDown(G1)

# Laplacian Pyramid
L0 = G0 - cv2.pyrUp(G1)
L1 = G1 - cv2.pyrUp(G2)

print(f"L0.shape =\n{L0.shape}")
print(f"L1.shape =\n{L1.shape}")

cv2.imshow('Laplacian L0', L0)
cv2.imshow('Laplacian L1', L1)

cv2.waitKey(0)
cv2.destroyAllWindows()
