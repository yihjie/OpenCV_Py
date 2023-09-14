import cv2

src = cv2.imread('3heart.jpg')
src_copy = src.copy()

src_gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
dst = cv2.drawContours(src, contours, -1, (0, 255,0), 5)

M0 = cv2.moments(contours[0])
M1 = cv2.moments(contours[1])
M2 = cv2.moments(contours[2])
Hu0 = cv2.HuMoments(M0)
Hu1 = cv2.HuMoments(M1)
Hu2 = cv2.HuMoments(M2)

for i in range(len(contours)):
    M = cv2.moments(contours[i])
    Cx = int(M['m10'] / M['m00'])
    Cy = int(M['m01'] / M['m00'])
    cv2.putText(dst, str(i), (Cx - 3, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)

print(f"h0 = {Hu0[0]}\t\t\t {Hu1[0]}\t\t\t {Hu2[0]}")
print(f"h1 = {Hu0[1]}\t\t\t {Hu1[1]}\t\t\t {Hu2[1]}")
print(f"h2 = {Hu0[2]}\t\t\t {Hu1[2]}\t\t\t {Hu2[2]}")
print(f"h3 = {Hu0[3]}\t\t\t {Hu1[3]}\t\t\t {Hu2[3]}")
print(f"h4 = {Hu0[4]}\t\t\t {Hu1[4]}\t\t\t {Hu2[4]}")
print(f"h5 = {Hu0[5]}\t\t\t {Hu1[5]}\t\t\t {Hu2[5]}")
print(f"h6 = {Hu0[6]}\t\t\t {Hu1[6]}\t\t\t {Hu2[6]}")

cv2.imshow('Result', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
