import cv2

src = cv2.imread('easy.jpg')
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 5)

n = len(contours)
for i in range(n):
    M = cv2.moments(contours[i])
    Cx = int(M['m10'] / M['m00'])
    Cy = int(M['m01'] / M['m00'])
    area = cv2.contourArea(contours[i]) # 面積
    cv2.putText(dst, str(i), (Cx - 3, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(dst, str(area), (Cx - 25, int(src.shape[0] / 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)

cv2.imshow('Result', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
